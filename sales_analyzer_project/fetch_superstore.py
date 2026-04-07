# fetch_superstore.py - SIMPLIFIED VERSION (No Kaggle required)
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

print("="*60)
print("🏪 GENERATING SUPERSTORE DATA")
print("="*60)

# Create directories
os.makedirs('data', exist_ok=True)
os.makedirs('models', exist_ok=True)

print("📅 Generating 2 years of daily sales data...")

# Generate date range
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# Set random seed for reproducibility
np.random.seed(42)

data = []
for date in dates:
    # Base sales with trend (increasing over time)
    days_since_start = (date - start_date).days
    trend = days_since_start * 3  # $3 increase per day
    
    # Seasonality
    month = date.month
    if month == 12:  # December holiday peak
        seasonal = 1.6
    elif month == 11:  # November
        seasonal = 1.3
    elif month == 1:  # January
        seasonal = 0.8
    elif month == 7:  # July
        seasonal = 1.2
    else:
        seasonal = 1.0
    
    # Day of week pattern
    dow = date.dayofweek
    if dow >= 5:  # Weekend
        dow_factor = 1.4
    elif dow == 0:  # Monday
        dow_factor = 0.9
    elif dow == 4:  # Friday
        dow_factor = 1.2
    else:
        dow_factor = 1.0
    
    # Random noise
    noise = np.random.normal(1, 0.12)
    
    # Calculate sales
    base_sales = 4000 + trend
    sales = base_sales * seasonal * dow_factor * noise
    
    # Calculate other metrics
    customers = int(sales / 70 + np.random.normal(0, 3))
    customers = max(15, customers)
    
    quantity = int(customers * np.random.uniform(1.2, 2.2))
    
    discount = np.random.choice([0, 0.05, 0.1, 0.15, 0.2], p=[0.4, 0.2, 0.2, 0.15, 0.05])
    
    profit_margin = np.random.uniform(0.15, 0.35)
    profit = sales * profit_margin * (1 - discount * 0.5)
    
    # Regions and categories
    regions = ['East', 'West', 'Central', 'South']
    categories = ['Office Supplies', 'Technology', 'Furniture']
    segments = ['Consumer', 'Corporate', 'Home Office']
    
    data.append({
        'date': date,
        'sales': round(sales, 2),
        'profit': round(profit, 2),
        'discount': round(discount, 3),
        'quantity': quantity,
        'customers': customers,
        'region': np.random.choice(regions),
        'category': np.random.choice(categories),
        'segment': np.random.choice(segments),
        'day_of_week': dow,
        'month': month,
        'year': date.year,
        'is_weekend': 1 if dow >= 5 else 0,
        'is_holiday_season': 1 if month in [11, 12] else 0
    })

df = pd.DataFrame(data)

# Sort by date
df = df.sort_values('date').reset_index(drop=True)

# Add lag features
print("🔧 Creating lag features...")
df['sales_lag_1'] = df['sales'].shift(1)
df['sales_lag_7'] = df['sales'].shift(7)
df['sales_lag_30'] = df['sales'].shift(30)
df['sales_rolling_7'] = df['sales'].rolling(window=7, min_periods=1).mean()
df['sales_rolling_30'] = df['sales'].rolling(window=30, min_periods=1).mean()

# Fill NaN values (first few rows)
df = df.bfill().ffill()

# Save to CSV
df.to_csv('data/sales_data.csv', index=False)
print(f"✅ Data saved to: data/sales_data.csv")
print(f"   Rows: {len(df):,}")
print(f"   Date range: {df['date'].min().date()} to {df['date'].max().date()}")

# Print summary
print("\n📊 DATA SUMMARY:")
print(f"   Total Sales: ${df['sales'].sum():,.2f}")
print(f"   Average Daily: ${df['sales'].mean():,.2f}")
print(f"   Best Day: ${df['sales'].max():,.2f}")
print(f"   Total Customers: {df['customers'].sum():,.0f}")
print(f"   Total Profit: ${df['profit'].sum():,.2f}")

print("\n✅ Data generation complete!")
print("\nNext step: Run 'python train_model.py'")