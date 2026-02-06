# Campaign Performance Helper - Project Plan

## Problem

As a PPC manager, I manually export campaign performance data from Google Ads every week, then spend 30 minutes copying it into a spreadsheet and calculating basic metrics. This is repetitive and error-prone.

## Goal

Create a simple Python script that automatically fetches last 7 days of campaign performance data and saves it to a CSV file I can open in Excel or Google Sheets.

## Data Sources

- **Google Ads API** — We'll use the reporting API to pull campaign-level metrics
  - Campaigns (name, ID, status)
  - Impressions, Clicks, Cost
  - Conversions, Conversion Value

## Rough Flow

1. **Load credentials** from environment variables (never hardcode API keys)
2. **Connect to Google Ads API** using the authentication token
3. **Query last 7 days** of campaign data for our account
4. **Calculate extra metrics** like CTR (click-through rate) and CPA (cost per acquisition)
5. **Save to CSV file** in the `data/` folder with today's date in filename

## Security Notes

- **Never commit API keys** — use `.env` file and add it to `.gitignore`
- Store the `.env.example` template in git so teammates know what variables are needed
- Use read-only API permissions when possible
- Keep the `data/` folder in `.gitignore` — it may contain sensitive performance data

## Files We Expect

```
campaign-helper/
├── main.py              # Main script that does the work
├── .env                 # Your actual credentials (NOT in git)
├── .env.example         # Template showing what credentials are needed (in git)
├── .gitignore           # Tells git to ignore secrets and output files
├── PLAN.md              # This file
└── data/                # Where CSV reports are saved (NOT in git)
    └── campaigns_2024-01-15.csv
```

## Next Steps

- Set up Google Ads API access (OAuth 2.0)
- Copy `.env.example` to `.env` and fill in real credentials
- Run `python main.py` to generate first report
- Schedule it to run automatically (future enhancement)