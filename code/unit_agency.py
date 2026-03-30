import duckdb
import os
import logging

# Same logging set up 
logging.basicConfig(
    filename='/content/drive/MyDrive/DS_data/pipeline.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run():
    """
    Uses DuckDB to extract unique administrative units and map them to 
    formal agency names, creating a relational dimension table for normalization.
    """
    logging.info("Starting unit_agency dimension mapping...")

    base_path = '/content/drive/MyDrive/DS_data/'
    fire_in = os.path.join(base_path, 'wildfire_events.parquet')
    agency_out = os.path.join(base_path, 'unit_agency.parquet')

    # Proper error handling
    # Making sure the mapping script doesn't fail due to missing upstream parquet files
    if not os.path.exists(fire_in):
        logging.error(f"CRITICAL: Upstream file missing at {fire_in}")
        print(f"Error: Check log file. The wildfire_events entity must be created first.")
        return

    # Processing logic with exception handling
    try:
        # Initializing an in-memory DuckDB connection for Parquet processing
        con = duckdb.connect()
        
        logging.info("DuckDB connection established. Executing SQL mapping...")

        # SQL logic: normalizing shorthand unit IDs into descriptive agency names
        con.execute(f"""
            COPY (
                -- Extracting unique fire unit identifiers.
                -- Mapping shorthand codes to full agency names for better readability
                -- in the final publication-quality visualizations.
                SELECT DISTINCT Unit_ID,
                    CASE
                      WHEN Unit_ID = 'VNC' THEN 'Ventura County Fire'
                      WHEN Unit_ID = 'LAC' THEN 'Los Angeles County Fire'
                      WHEN Unit_ID = 'SBC' THEN 'Santa Barbara County Fire'
                      WHEN Unit_ID = 'BDU' THEN 'San Bernardino Unit'
                      WHEN Unit_ID = 'RRU' THEN 'Riverside Unit'
                      ELSE 'Regional Fire Authority'
                    END AS Agency_Name
                FROM read_parquet('{fire_in}')
            ) TO '{agency_out}' (FORMAT 'PARQUET') 
        """)

        logging.info(f"SUCCESS: unit_agency dimension table exported to {agency_out}")
        print("Entity created successfully.")

    except Exception as e:
        # Catch-all for errors
        logging.error(f"Unexpected error during agency mapping: {str(e)}")
        print("Agency mapping failed. Check pipeline.log for details.")
    
    finally:
        # Making sure DuckDB connection is closed to prevent file locks
        con.close()

run()
