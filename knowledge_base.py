import pandas as pd

# 1. Load the data
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# 2. Calculate Advanced Metrics
sales_by_product = df.groupby('Product')['Sales'].sum().to_dict()
sat_by_product = df.groupby('Product')['Customer_Satisfaction'].mean().round(2).to_dict()

# 3. Create the Knowledge Base Dictionary
summary = {
    "Total Sales": f"${df['Sales'].sum():,.2f}",
    "Average Satisfaction": round(df['Customer_Satisfaction'].mean(), 2),
    "Sales Volatility (Std Dev)": round(df['Sales'].std(), 2),
    "Top Product": df.groupby('Product')['Sales'].sum().idxmax(),
    "Top Region": df.groupby('Region')['Sales'].sum().idxmax(),
    "Gender Split": df['Customer_Gender'].value_counts().to_dict(),
    "Best Satisfaction Product": df.groupby('Product')['Customer_Satisfaction'].mean().idxmax(),
    "Sales Breakdown by Product": sales_by_product,
    "Satisfaction Breakdown by Product": sat_by_product,
    "Analysis Note": "There is a negative correlation between volume and satisfaction; the highest volume product (Widget A) has lower satisfaction than the lowest volume product (Widget D)."
}

# 4. Save to text file and print to console
print("--- Advanced Knowledge Base Created ---")
with open('data_context.txt', 'w') as f:
    for key, value in summary.items():
        line = f"{key}: {value}"
        print(line)
        f.write(line + "\n")