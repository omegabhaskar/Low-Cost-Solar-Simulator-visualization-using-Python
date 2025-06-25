import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def fetch_data_from_api(latitude, longitude, start_date, end_date):
    """
    Fetches solar intensity and temperature data from the NASA POWER API.
    """
    url = (f"https://power.larc.nasa.gov/api/temporal/hourly/point?"
           f"start={start_date}&end={end_date}&latitude={latitude}&longitude={longitude}&community=RE"
           f"&parameters=ALLSKY_SFC_SW_DWN,T2M&format=JSON")
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def transform_data(data):
    """
    Processes the raw data into a DataFrame for analysis.
    """
    if data and 'properties' in data and 'parameter' in data['properties']:
        solar_data = data['properties']['parameter'].get('ALLSKY_SFC_SW_DWN', {})
        temp_data = data['properties']['parameter'].get('T2M', {})
        
        timestamps = [datetime.strptime(ts, '%Y%m%d%H') for ts in solar_data.keys()]
        solar_values = list(solar_data.values())
        temp_values = [temp_data.get(ts, pd.NA) for ts in solar_data.keys()]
        
        df = pd.DataFrame({
            'Timestamp': timestamps,
            'Solar Intensity (W/m²)': solar_values,
            'Temperature (°C)': temp_values
        })
        
        df['Date'] = df['Timestamp'].dt.strftime('%-d %b, %Y')
        df['12-Hour Format'] = df['Timestamp'].dt.strftime('%I:%M %p')
        df.drop(columns=['Timestamp'], inplace=True)
        df['Solar Intensity (W/m²)'] = df['Solar Intensity (W/m²)'].replace(-999, pd.NA)
        df['Temperature (°C)'] = df['Temperature (°C)'].replace(-999, pd.NA)
        
        return df
    else:
        print("No valid data found in the API response.")
        return None

def save_data_to_excel(df, filename):
    """
    Saves the DataFrame to an Excel file.
    """
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

def plot_data(df):
    """
    Plots the solar intensity and temperature data.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df['12-Hour Format'], df['Solar Intensity (W/m²)'], marker='o', label='Solar Intensity (W/m²)')
    plt.plot(df['12-Hour Format'], df['Temperature (°C)'], marker='x', label='Temperature (°C)', linestyle='--')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Solar Intensity and Temperature Over Time')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to get user input, fetch, process, and display data.
    """
    try:
        latitude, longitude = map(float, input("Enter the latitude and longitude (comma-separated): ").split(','))
    except ValueError:
        print("Please enter valid numerical values for latitude and longitude.")
        return
    
 
    date_input = input("Enter the date (DD-MM-YYYY): ")
    try:
        date = datetime.strptime(date_input, '%d-%m-%Y')
        formatted_date = date.strftime('%Y%m%d')
    except ValueError:
        print("Invalid date format. Use DD-MM-YYYY.")
        return
    
    data = fetch_data_from_api(latitude, longitude, formatted_date, formatted_date)
    df = transform_data(data)

    if df is not None and not df['Solar Intensity (W/m²)'].isna().all():
        filename = 'solar_intensity_and_temperature.xlsx'
        save_data_to_excel(df, filename)
        print(df)
        plot_data(df)
    else:
        print("No data available for the specified date and location.")

if __name__ == "__main__":
    main()

# Modules required are openpyxl, requests, pandas, matplotlib.