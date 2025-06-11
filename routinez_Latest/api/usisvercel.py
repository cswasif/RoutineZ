import requests
import json
import time

def load_data():
    global data
    if data is None:
        try:
            DATA_URL = "https://connapi.vercel.app/raw-schedule"
            print(f"\nLoading data from {DATA_URL}...")

            # Add retry logic
            max_retries = 3
            retry_delay = 2  # seconds

            for attempt in range(max_retries):
                try:
                    print(f"Attempt {attempt + 1}/{max_retries}...")
                    response = requests.get(DATA_URL, timeout=10)
                    response.raise_for_status()
                    raw_json = response.json()
                    # Use only the 'data' key from the response
                    if isinstance(raw_json, dict) and "data" in raw_json:
                        data = raw_json["data"]
                    else:
                        print(f"Warning: Expected dict with 'data' key, got {type(raw_json)}")
                        continue

                    if not isinstance(data, list):
                        print(f"Warning: Expected list data, got {type(data)}")
                        continue

                    print(f"Successfully loaded {len(data)} sections")
                    return data

                except (
                    requests.exceptions.RequestException,
                    json.JSONDecodeError,
                ) as e:
                    print(f"Error on attempt {attempt + 1}: {e}")
                    if attempt < max_retries - 1:
                        print(f"Retrying in {retry_delay} seconds...")
                        time.sleep(retry_delay)
                    continue

            print("All retry attempts failed. Setting data to empty list.")
            data = []
            return data

        except Exception as e:
            print(f"Critical error in load_data: {e}")
            print("Setting data to empty list.")
            data = []
            return data
    return data 