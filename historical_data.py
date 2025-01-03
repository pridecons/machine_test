import os
import pandas as pd
from kiteconnect import KiteConnect
from config import API_KEY, API_SECRET

ACCESS_TOKEN_FILE = "access_token.txt"

def generate_access_token():
    """
    Generate a new access token using Kite Connect.
    """
    kite = KiteConnect(api_key=API_KEY)
    print("Login URL:", kite.login_url())
    request_token = input("Paste the 'request_token' here: ")
    data = kite.generate_session(request_token, api_secret=API_SECRET)
    access_token = data["access_token"]

    with open(ACCESS_TOKEN_FILE, "w") as f:
        f.write(access_token)
    print("Access Token saved to file.")
    return access_token

def get_access_token():
    """
    Read the saved access token from the file.
    """
    if not os.path.exists(ACCESS_TOKEN_FILE):
        print("Access token not found. Generate a new token.")
        return generate_access_token()

    with open(ACCESS_TOKEN_FILE, "r") as f:
        return f.read().strip()

def fetch_historical_data(kite, instrument_token, from_date, to_date, interval="day"):
    """
    Fetch historical data for a given instrument token.
    """
    try:
        print(f"Fetching historical data for token {instrument_token}...")
        data = kite.historical_data(instrument_token, from_date, to_date, interval)
        df = pd.DataFrame(data)
        print(f"Fetched {len(df)} rows of historical data.")
        return df
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return None

def save_to_csv(dataframe, filename):
    """
    Save a DataFrame to a CSV file.
    """
    try:
        dataframe.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

def main():
    """
    Main function to fetch historical data and save it to CSV.
    """
    access_token = get_access_token()

    kite = KiteConnect(api_key=API_KEY)
    kite.set_access_token(access_token)

    # Example instrument token for Reliance (check the instrument token for your stock)
    instrument_token = 884737  # Replace with the token for your stock
    from_date = "2023-12-01"
    to_date = "2025-01-01"
    interval = "day"  # Options: minute, day, 5minute, 15minute, etc.

    historical_data = fetch_historical_data(kite, instrument_token, from_date, to_date, interval)

    if historical_data is not None:
        output_csv = "historical_data.csv"
        save_to_csv(historical_data, output_csv)

if __name__ == "__main__":
    main()
