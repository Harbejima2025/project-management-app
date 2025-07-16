import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def get_sheet_data(sheet_name):
    # Step 1: Define the required scopes
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # Step 2: Authenticate using the service account credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)

    # Step 3: Open the spreadsheet
    sheet = client.open(sheet_name).sheet1  # This gets the first tab (worksheet)

    # Step 4: Get all data as list of dictionaries
    data = sheet.get_all_records()

    # Step 5: Convert to a pandas DataFrame
    df = pd.DataFrame(data)
    return df

# Optional: Run directly to test
if __name__ == "__main__":
    SHEET_NAME = "Your Sheet Name Here"  # Replace with your actual Google Sheet title
    df = get_sheet_data(SHEET_NAME)
    print("✅ Sheet Loaded Successfully")
    print(df.head())  # Show top 5 rows
