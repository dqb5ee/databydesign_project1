import pandas as pd
import os

# Configuring 
base_path = '/content/drive/MyDrive/DS_data/'

# Inputs: Using the files created by Step 1 and Step 2
moisture_input = os.path.join(base_path, 'processed_fuel_moisture.csv')
fires_input = os.path.join(base_path, 'filtered_socal_fires.csv')

# Output: The final master dataset for the project
master_output = os.path.join(base_path, 'fire_moisture_master.csv')

def create_master_dataset():
    print("Beginning Relational Join...")
    
    # Loading processed components
    if not os.path.exists(moisture_input) or not os.path.exists(fires_input):
        print("Error: Required processed files (moisture or fires) are missing.")
        return

    moisture = pd.read_csv(moisture_input)
    fires = pd.read_csv(fires_input)

    # Aligning datatypes for join
    # Ensuring both dataframes use the same 'Period' format for the join key
    moisture['month_yr'] = pd.to_datetime(moisture['month_yr']).dt.to_period('M')
    fires['month_yr'] = pd.to_datetime(fires['Alarm Date']).dt.to_period('M')

    # Performing join
    # This maps every fire event to the regional moisture level of that month
    master_df = pd.merge(fires, moisture, on='month_yr', how='left')

    # Exporting model
    master_df.to_csv(master_output, index=False)
    
    # Validation logic
    # Proving the join worked by checking the 'percent' column is populated
    valid_records = master_df.dropna(subset=['percent'])
    
    print("-" * 30)
    print(f"RELATIONAL JOIN SUCCESSFUL")
    print(f"Master Records Created: {len(master_df)}")
    print(f"Records with Valid Moisture Correlation: {len(valid_records)}")
    print(f"Final Output Saved: {master_output}")
    print("-" * 30)

if __name__ == "__main__":
    create_master_dataset()    # Calculating for proof of concept
    avg_moisture = major_fires['percent'].mean()
    pct_below_threshold = (major_fires[major_fires['percent'] <= 75].shape[0] / len(major_fires)) * 100

    print("-" * 30)
    print(f"VALIDATION SUCCESSFUL")
    print(f"Total Major Fires Analyzed: {len(major_fires)}")
    print(f"Average Moisture at Ignition: {avg_moisture:.2f}%")
    print(f"Percentage of Fires below 75% Threshold: {pct_below_threshold:.1f}%")
    print("-" * 30)

if __name__ == "__main__":
    run_validation()
