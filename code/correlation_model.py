import duckdb
import os
import pandas as pd
import logging

# Same logging as other scripts
logging.basicConfig(
    filename='/content/drive/MyDrive/DS_data/pipeline.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run():
    """
    This function executes the multi-table relational join via DuckDB.
    It serves as the final bridge between environmental baselines and historical fire events 
    to create a unified analytical dataset.
    """
    logging.info("Starting Arid Edge relational join...")

    # Defining the data directory for Google Colab
    data_dir = '/content/drive/MyDrive/DS_data/'
    
    # Proper error handling
    # Making sure all required Parquet entities exist before attempting the join
    required_files = ["wildfire_events.parquet", "unit_agency.parquet", "moisture_readings.parquet"]
    for f in required_files:
        if not os.path.exists(os.path.join(data_dir, f)):
            logging.error(f"CRITICAL: Missing dependency {f}")
            print(f"Error: Missing {f}. Run previous transformation steps first.")
            return

    # Processing Logic with Exception Handling
    try:
        # Initializing an in-memory DuckDB connection
        con = duckdb.connect()
        logging.info("DuckDB connection initialized for multi-table join.")

        # SQL join logic:
        # Joining "wildfire_events" (fact table) to 'unit_agency' (dimension table) via Unit_ID
        # Joining "wildfire_events" to "moisture_readings" (fact table) via a temporal join
        # This matches Alarm_Date to the regional moisture baseline at a Month-Year level
        query = f"""
            SELECT 
                f.Fire_Name, 
                f.Alarm_Date, 
                f.GIS_Acres, 
                r.LFM_Percent, 
                a.Agency_Name
            FROM read_parquet('{os.path.join(data_dir, "wildfire_events.parquet")}') f
            JOIN read_parquet('{os.path.join(data_dir, "unit_agency.parquet")}') a 
                 ON f.Unit_ID = a.Unit_ID
            JOIN read_parquet('{os.path.join(data_dir, "moisture_readings.parquet")}') r 
                 ON strftime(f.Alarm_Date, '%Y-%m') = strftime(r.Date, '%Y-%m')
            ORDER BY f.GIS_Acres DESC
        """
        
        # Executing the relational query and converting the result set into a pandas df
        # This satisfies the requirement for creating a solution through queries
        results = con.execute(query).df()
        logging.info(f"Join complete. Analytical dataset created with {len(results)} records.")

        # Exporting the final analytical entity to Parquet 
        output_path = os.path.join(data_dir, 'final_arid_edge_analysis.parquet')
        results.to_parquet(output_path, index=False)
        
        logging.info(f"SUCCESS: Final analytical entity exported to {output_path}")
        print("Entity created successfully.")
        return results

    except Exception as e:
        # Catch-all for SQL syntax issues or memory errors during the join
        logging.error(f"Unexpected error during relational join: {str(e)}")
        print("Relational join failed. Check pipeline.log for details.")
    
    finally:
        con.close()

if __name__ == "__main__":
    # Execute the join and store the result for the next cell (Random Forest modeling)
    df_analysis = run()
