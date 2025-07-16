from read_sheet import get_sheet_data

def analyze_data(df):
    print("\n🔍 Descriptive Statistics (Numerical Columns):")
    print(df.describe(include='all'))

    print("\n📊 Value Counts (Top 3 values per column):")
    for col in df.columns:
        print(f"\nColumn: {col}")
        print(df[col].value_counts().head(3))

    # Optional: Add more custom analysis
    # Example: total revenue if there are "Quantity" and "Price" columns
    if 'Quantity' in df.columns and 'Price' in df.columns:
        df['Revenue'] = df['Quantity'] * df['Price']
        print("\n💰 Total Revenue:")
        print(df['Revenue'].sum())

if __name__ == "__main__":
    SHEET_NAME = "Your Sheet Name Here"  # Replace with your sheet title
    df = get_sheet_data(SHEET_NAME)
    print("✅ Sheet Loaded. Starting analysis...\n")
    analyze_data(df)
