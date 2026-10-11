import requests
import os
import json

def get_intervals_data():
    api_key = os.getenv("INTERVALS_API_KEY")
    athlete_id = os.getenv("INTERVALS_ATHLETE_ID")

    url = f"https://intervals.icu/api/v1/athlete/{athlete_id}/metrics"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # Save to file
    with open("intervals_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Intervals data collected successfully.")

if __name__ == "__main__":
    get_intervals_data()
