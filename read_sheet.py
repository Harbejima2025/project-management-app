import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def get_sheet_data(sheet_name):
    # Define the scopes
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Authorize using the service account credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)

    # Open the spreadsheet and get the first worksheet
    sheet = client.open(sheet_name).sheet1

    # Get all records as a list of dictionaries
    records = sheet.get_all_records()
    return pd.DataFrame(records)

if __name__ == "__main__":
    sheet_name = "YOUR GOOGLE SHEET NAME HERE"
    df = get_sheet_data(sheet_name)
    print(df.head())
