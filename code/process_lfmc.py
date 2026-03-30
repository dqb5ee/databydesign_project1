import pandas as pd
import os

def run():
    # Defining relative paths to fit GitHub syntax
    base_path = '/content/drive/MyDrive/DS_data/'
    input_file = os.path.join(base_path, 'lfmc_observations.csv')

    # Loading and transforming
    df = pd.read_csv(input_file)

    # Creating moisture_site entity
    sites = df[['site', 'latitude', 'longitude']].drop_duplicates()
    sites.columns = ['Site_ID', 'Latitude', 'Longitude']
    sites.to_parquet(os.path.join(base_path, 'moisture_sites.parquet'), index=False)

    # Creating moisture_reading entity
    readings = df[['site', 'date', 'percent', 'fuel']].copy()
    readings.columns = ['Site_ID', 'Date', 'LFM_Percent', 'Fuel_Type']
    readings['Date'] = pd.to_datetime(readings['Date'])

    # Filtering for study period
    readings = readings[(readings['Date'] >= '2005-01-01') & (readings['Date'] <= '2019-06-30')]
    readings['Reading_ID'] = range(1, len(readings) + 1)

    readings.to_parquet(os.path.join(base_path, 'moisture_readings.parquet'), index=False)
    print("Entities created successfully.")

run()
