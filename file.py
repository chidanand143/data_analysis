import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_FILENAME = 'sales_data.csv'
GROUPBY_COLUMN = 'Category'
VALUE_COLUMN = 'Sales_Amount'

print(f"--- 1. Loading Data: {CSV_FILENAME} ---")
try:
    if not os.path.exists(CSV_FILENAME):
        print(f"Error: File '{CSV_FILENAME}' not found in the current directory.")
        print("Please upload the file or update the CSV_FILENAME variable.")
        print("\nCreating dummy data for demonstration...")
        data = {
            'Date': pd.to_datetime(['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03']),
            GROUPBY_COLUMN: ['Electronics', 'Clothing', 'Electronics', 'Home Goods', 'Clothing'],
            VALUE_COLUMN: [1500.00, 50.00, 2500.00, 150.00, 90.00],
            'Product': ['Laptop', 'Shirt', 'Monitor', 'Lamp', 'Jeans']
        }
        df = pd.DataFrame(data)
    else:
        df = pd.read_csv(CSV_FILENAME)

    print(f"Successfully loaded {len(df)} rows.")
    print("\nInitial Data Check:")
    print(df.head())
    print("\nData Types:")
    df.info()

    df[VALUE_COLUMN] = pd.to_numeric(df[VALUE_COLUMN], errors='coerce')
    df.dropna(subset=[GROUPBY_COLUMN, VALUE_COLUMN], inplace=True)

    print(f"\nCleaned Data Check (after dropping NaNs): {len(df)} rows remain.")


    print(f"\n--- 2. Analysis: Total {VALUE_COLUMN} by {GROUPBY_COLUMN} ---")

    sales_summary = df.groupby(GROUPBY_COLUMN)[VALUE_COLUMN].sum().sort_values(ascending=False)

    print(f"\nTop 10 {GROUPBY_COLUMN} by Total {VALUE_COLUMN}:")
    print(sales_summary.head(10))

    plt.figure(figsize=(12, 6))

    sales_summary.plot(kind='bar', color='darkblue')

    plt.title(f'Total {VALUE_COLUMN} by {GROUPBY_COLUMN}', fontsize=16)
    plt.xlabel(GROUPBY_COLUMN, fontsize=12)
    plt.ylabel(f'Total {VALUE_COLUMN}', fontsize=12)
    
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    plt.show()

    print("\n--- Outcome: Basic data insights visualized successfully. ---")


except Exception as e:
    print(f"\nAn unexpected error occurred during execution: {e}")
    print("Please check your column names and file integrity.")
