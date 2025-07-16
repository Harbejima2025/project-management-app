from read_sheet import get_sheet_data

def analyze_data(df):
    print("\n🔍 Descriptive Statistics:")
    print(df.describe())

    print("\n📊 Column Summary:")
    for col in df.columns:
        print(f"\nColumn: {col}")
        print(df[col].value_counts().head())

if __name__ == "__main__":
    sheet_name = "YOUR GOOGLE SHEET NAME HERE"
    df = get_sheet_data(sheet_name)
    analyze_data(df)
