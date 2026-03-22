import pandas as pd
import os

# Configurating
base_path = '/content/drive/MyDrive/DS_data/'
input_path = os.path.join(base_path, 'lfmc_observations.csv')
output_path = os.path.join(base_path, 'processed_fuel_moisture.csv')

def process_moisture():
    # Loading data
    if not os.path.exists(input_path):
        print(f"Error: Could not find {input_path}")
        return

    df = pd.read_csv(input_path)
    
    # Making sure "date" is in datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Filtering for study period (2005 - 2019)
    # This captures the critical window for Southern California wildfire analysis
    df = df[(df['date'] >= '2005-01-01') & (df['date'] <= '2019-06-30')]

    # Aggregating to monthly regional average
    # This transforms 10,000+ individual readings into a 'Landscape Reservoir' baseline
    df['month_yr'] = df['date'].dt.to_period('M')
    moisture_baseline = df.groupby('month_yr')['percent'].mean().reset_index()

    # Saving processed data
    # Creating the folder if it doesn't exist to prevent errors
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    moisture_baseline.to_csv(output_path, index=False)
    
    print(f"Success: {output_path} created with {len(moisture_baseline)} monthly records.")

if __name__ == "__main__":
    process_moisture()
