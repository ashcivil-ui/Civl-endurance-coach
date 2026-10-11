import os
import json
import requests

def get_calendar_events():
    calendar_api_key = os.getenv("CALENDAR_API_KEY")
    calendar_id = os.getenv("CALENDAR_ID")

    url = f"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"

    params = {
        "key": calendar_api_key,
        "singleEvents": True,
        "orderBy": "startTime",
        "timeMin": "2024-01-01T00:00:00Z",
        "timeMax": "2025-12-31T23:59:59Z"
    }

    response = requests.get(url, params=params)
    events = response.json()

    with open("calendar_data.json", "w") as f:
        json.dump(events, f, indent=2)

    print("Calendar data collected successfully.")

if __name__ == "__main__":
    get_calendar_events()
