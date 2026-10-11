import requests
import os
import json

def get_strava_activities():
    client_id = os.getenv("STRAVA_CLIENT_ID")
    client_secret = os.getenv("STRAVA_CLIENT_SECRET")
    refresh_token = os.getenv("STRAVA_REFRESH_TOKEN")

    # Step 1: Refresh the access token
    token_url = "https://www.strava.com/oauth/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }

    response = requests.post(token_url, data=payload)
    response_data = response.json()
    access_token = response_data["access_token"]

    # Step 2: Get activities
    activities_url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {"Authorization": f"Bearer {access_token}"}

    activities_response = requests.get(activities_url, headers=headers)
    activities = activities_response.json()

    # Save to file
    with open("strava_data.json", "w") as f:
        json.dump(activities, f, indent=2)

    print("Strava data collected successfully.")

if __name__ == "__main__":
    get_strava_activities()
