import os
import json
import anthropic

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def generate_weekly_plan():
    # Load your collected data
    strava_data = load_json("strava_data.json")
    intervals_data = load_json("intervals_data.json")
    calendar_data = load_json("calendar_data.json")

    # Claude client
    client = anthropic.Anthropic(
        api_key=os.getenv("CLAUDE_API_KEY")
    )

    # Build the prompt
    prompt = f"""
You are an endurance coach creating a weekly training plan.

Here is the athlete's data:

STRAVA DATA:
{json.dumps(strava_data, indent=2)}

INTERVALS FATIGUE / LOAD DATA:
{json.dumps(intervals_data, indent=2)}

CALENDAR AVAILABILITY:
{json.dumps(calendar_data, indent=2)}

Create a 7‑day training plan that:
- Fits around the calendar availability
- Adjusts based on fatigue and readiness
- Uses Strava history to set intensities
- Includes run, bike, strength, mobility
- Includes recovery guidance
- Includes pacing targets
- Includes HR zones
- Includes session purpose
- Includes total weekly load

Return the plan in clean JSON with fields:
- day
- session_type
- duration_minutes
- description
- intensity
- notes
"""

    # Claude call
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=2000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    plan = response.content[0].text

    # Save the plan
    with open("weekly_plan.json", "w") as f:
        f.write(plan)

    print("Weekly plan generated and saved.")

if __name__ == "__main__":
    generate_weekly_plan()
