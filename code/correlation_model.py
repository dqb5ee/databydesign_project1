import duckdb
import os
import pandas as pd

def run():
    data_dir = os.path.join('..', 'data')
    con = duckdb.connect()
    
    # Join logic to produce the final analytical entity
    query = f"""
        SELECT f.Fire_Name, f.Alarm_Date, f.GIS_Acres, r.LFM_Percent, a.Agency_Name
        FROM read_parquet('{os.path.join(data_dir, "wildfire_events.parquet")}') f
        JOIN read_parquet('{os.path.join(data_dir, "unit_agency.parquet")}') a ON f.Unit_ID = a.Unit_ID
        JOIN read_parquet('{os.path.join(data_dir, "moisture_readings.parquet")}') r 
             ON strftime(f.Alarm_Date, '%Y-%m') = strftime(r.Date, '%Y-%m')
    """
    
    results = con.execute(query).df()
    results.to_parquet(os.path.join(data_dir, 'final_arid_edge_analysis.parquet'), index=False)
    print("Final analytical join complete and saved to Parquet.")

if __name__ == "__main__": run()
