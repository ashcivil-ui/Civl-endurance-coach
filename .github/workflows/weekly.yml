name: Weekly Endurance Plan

on:
  schedule:
    - cron: "0 18 * * 0"
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          pip install requests anthropic

      - name: Run Strava collector
        env:
          STRAVA_CLIENT_ID: ${{ secrets.STRAVA_CLIENT_ID }}
          STRAVA_CLIENT_SECRET: ${{ secrets.STRAVA_CLIENT_SECRET }}
          STRAVA_REFRESH_TOKEN: ${{ secrets.STRAVA_REFRESH_TOKEN }}
        run: python strava_collector.py

      - name: Run Intervals collector
        env:
          INTERVALS_API_KEY: ${{ secrets.INTERVALS_API_KEY }}
        run: python intervals_collector.py

      - name: Run Calendar collector
        env:
          CALENDAR_API_KEY: ${{ secrets.CALENDAR_API_KEY }}
          CALENDAR_ID: ${{ secrets.CALENDAR_ID }}
        run: python calendar_collector.py

      - name: Generate weekly plan
        env:
          CLAUDE_API_KEY: ${{ secrets.CLAUDE_API_KEY }}
        run: python generate_plan.py

      - name: Commit weekly plan
        run: |
          git config user.name "github-actions"
          git config user.email "actions@github.com"
          git add weekly_plan.json
          git commit -m "Weekly plan update"
          git push
