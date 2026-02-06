"""
Campaign Performance Helper - Demo Script

This is a simplified demo showing best practices:
- Loading credentials from environment variables
- Never hardcoding API keys
- Saving output to a separate data directory
- Using mock data for workshop demonstration
"""

import os
import csv
from datetime import datetime
from pathlib import Path

# Step 1: Load environment variables
# In a real script, you'd load from .env using python-dotenv package
# For this demo, we just check that the variables exist
try:
    api_key = os.environ.get("GOOGLE_ADS_API_KEY", "demo-key-not-set")
    client_id = os.environ.get("GOOGLE_ADS_CLIENT_ID", "demo-client-not-set")
    customer_id = os.environ.get("GOOGLE_ADS_CUSTOMER_ID", "1234567890")
    output_dir = os.environ.get("OUTPUT_DIR", "./data")
except KeyError as e:
    print(f"ERROR: Missing required environment variable: {e}")
    print("Please copy .env.example to .env and fill in your credentials")
    exit(1)

print("Campaign Performance Helper")
print("=" * 50)
print(f"Customer ID: {customer_id}")
print(f"Output directory: {output_dir}")
print()

# Step 2: Mock function that would normally call the Google Ads API
def fetch_campaign_data():
    """
    In a real script, this would use the Google Ads API.
    For demo purposes, we return mock data.
    """
    print("Fetching campaign data... (mock data)")

    # Mock data representing 3 campaigns
    return [
        {"campaign": "Brand Search", "impressions": 15234, "clicks": 892, "cost": 445.50, "conversions": 23},
        {"campaign": "Generic Keywords", "impressions": 42156, "clicks": 1204, "cost": 1876.25, "conversions": 18},
        {"campaign": "Competitor Terms", "impressions": 8932, "clicks": 234, "cost": 312.80, "conversions": 5},
    ]

# Step 3: Fetch and process data
campaigns = fetch_campaign_data()

# Step 4: Calculate additional metrics
for campaign in campaigns:
    campaign["ctr"] = round((campaign["clicks"] / campaign["impressions"]) * 100, 2)
    campaign["cpa"] = round(campaign["cost"] / campaign["conversions"], 2) if campaign["conversions"] > 0 else 0

# Print summary table
print("\nCampaign Performance Summary:")
print("-" * 80)
print(f"{'Campaign':<25} {'Impr':>10} {'Clicks':>8} {'CTR %':>8} {'Cost':>10} {'Conv':>6} {'CPA':>8}")
print("-" * 80)
for c in campaigns:
    print(f"{c['campaign']:<25} {c['impressions']:>10,} {c['clicks']:>8,} {c['ctr']:>8} ${c['cost']:>9,.2f} {c['conversions']:>6} ${c['cpa']:>7,.2f}")
print("-" * 80)

# Step 5: Save to CSV file
Path(output_dir).mkdir(exist_ok=True)
today = datetime.now().strftime("%Y-%m-%d")
output_file = f"{output_dir}/campaigns_{today}.csv"

with open(output_file, "w", newline="") as f:
    fieldnames = ["campaign", "impressions", "clicks", "ctr", "cost", "conversions", "cpa"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(campaigns)

print(f"\nReport saved to: {output_file}")
print("You can now open this file in Excel or Google Sheets!")