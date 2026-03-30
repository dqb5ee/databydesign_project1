import duckdb
import os

def run():
    base_path = '/content/drive/MyDrive/DS_data/'

    # Defining input (raw wildfire data) and output (mapped agency data) paths
    fire_in = os.path.join(base_path, 'wildfire_events.parquet')
    agency_out = os.path.join(base_path, 'unit_agency.parquet')

    con = duckdb.connect()
    con.execute(f"""
            /* Extracting unique fire unit identifiers.
                Then mapping shorthand codes to full agency names for better readability
                in final visualizations
            */
        COPY (
            -- Extract unique Unit_IDs and map them to full Agency Names
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
        ) TO '{agency_out}' (FORMAT 'PARQUET') -- Export the mapping as a new Parquet file
    """)

    print("Entity created successfully.")

run()
