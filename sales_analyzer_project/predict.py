import pandas as pd
import numpy as np
import joblib
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os
import json

print("="*60)
print("🔮 FORECAST GENERATOR")
print("="*60)

# Create outputs directory
os.makedirs('outputs', exist_ok=True)

# Load model and feature list
print("\n📂 Loading model and data...")

# Check if model exists
if not os.path.exists('models/sales_model.pkl'):
    print("❌ Model not found! Please run train_model.py first.")
    exit()

model = joblib.load('models/sales_model.pkl')

# Load feature columns
with open('models/feature_cols.json', 'r') as f:
    feature_cols = json.load(f)

# Load latest data
df = pd.read_csv('data/sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date').reset_index(drop=True)

print(f"✅ Model loaded successfully")
print(f"📅 Last data date: {df['date'].max()}")

# Get latest data for features
latest_data = df.tail(60).copy()

# Generate future dates
last_date = df['date'].max()
future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=30)

print(f"\n📅 Generating forecast for next 30 days...")

# Make predictions
predictions = []
lower_bounds = []
upper_bounds = []

for i, date in enumerate(future_dates):
    # Create features dictionary with only the columns the model expects
    features = {}
    
    # Add time-based features (these are always available)
    if 'day_of_week' in feature_cols:
        features['day_of_week'] = date.dayofweek
    if 'month' in feature_cols:
        features['month'] = date.month
    if 'year' in feature_cols:
        features['year'] = date.year
    if 'is_weekend' in feature_cols:
        features['is_weekend'] = 1 if date.dayofweek >= 5 else 0
    if 'is_holiday_season' in feature_cols:
        features['is_holiday_season'] = 1 if date.month in [11, 12] else 0
    
    # Add business features (using averages from recent data)
    if 'discount' in feature_cols:
        features['discount'] = latest_data['discount'].mean()
    if 'quantity' in feature_cols:
        features['quantity'] = int(latest_data['quantity'].mean())
    if 'customers' in feature_cols:
        features['customers'] = int(latest_data['customers'].mean())
    
    # Add lag features (need to handle initial days carefully)
    if 'sales_lag_1' in feature_cols:
        if i == 0:
            features['sales_lag_1'] = latest_data['sales'].iloc[-1]
        else:
            features['sales_lag_1'] = predictions[i-1]
    
    if 'sales_lag_7' in feature_cols:
        if i < 7:
            # Use historical data for initial lags
            features['sales_lag_7'] = latest_data['sales'].iloc[-7 + i] if (i < 7) else predictions[i-7]
        else:
            features['sales_lag_7'] = predictions[i-7]
    
    if 'sales_lag_30' in feature_cols:
        if i < 30:
            features['sales_lag_30'] = latest_data['sales'].iloc[-30 + i] if (i < 30) else predictions[i-30]
        else:
            features['sales_lag_30'] = predictions[i-30]
    
    # Add rolling features
    if 'sales_rolling_7' in feature_cols:
        if i == 0:
            features['sales_rolling_7'] = latest_data['sales'].iloc[-7:].mean()
        else:
            # Combine historical and predicted for rolling average
            historical_part = latest_data['sales'].iloc[-(7-i):] if i < 7 else []
            predicted_part = predictions[max(0, i-7):i]
            combined = list(historical_part) + list(predicted_part)
            features['sales_rolling_7'] = np.mean(combined) if combined else latest_data['sales'].mean()
    
    if 'sales_rolling_30' in feature_cols:
        if i == 0:
            features['sales_rolling_30'] = latest_data['sales'].tail(30).mean()
        else:
            # Use latest data plus predictions for rolling average
            historical_part = latest_data['sales'].iloc[-(30-i):] if i < 30 else []
            predicted_part = predictions[max(0, i-30):i]
            combined = list(historical_part) + list(predicted_part)
            features['sales_rolling_30'] = np.mean(combined) if combined else latest_data['sales'].mean()
    
    # Create DataFrame with correct feature order
    features_df = pd.DataFrame([{col: features.get(col, 0) for col in feature_cols}])
    
    # Predict
    pred = model.predict(features_df)[0]
    predictions.append(pred)
    
    # Confidence intervals (±15% for now, could be improved)
    lower_bounds.append(pred * 0.85)
    upper_bounds.append(pred * 1.15)

# Create forecast DataFrame
forecast_df = pd.DataFrame({
    'date': future_dates,
    'predicted_sales': predictions,
    'lower_bound': lower_bounds,
    'upper_bound': upper_bounds
})

# Save forecast
forecast_path = 'outputs/30_day_forecast.csv'
forecast_df.to_csv(forecast_path, index=False)
print(f"\n✅ Forecast saved to: {forecast_path}")

# Display forecast summary
print("\n📊 30-DAY FORECAST SUMMARY")
print("-" * 50)
print(f"Total 30-day revenue: ${sum(predictions):,.2f}")
print(f"Average daily: ${np.mean(predictions):,.2f}")
print(f"Peak day: ${max(predictions):,.2f} on {future_dates[np.argmax(predictions)].strftime('%Y-%m-%d')}")
print(f"Lowest day: ${min(predictions):,.2f} on {future_dates[np.argmin(predictions)].strftime('%Y-%m-%d')}")

# Plot forecast
plt.figure(figsize=(14, 7))

# Plot historical (last 60 days)
historical = df.tail(60)
plt.plot(historical['date'], historical['sales'], 
         label='Historical Sales', color='blue', linewidth=2, marker='o', markersize=4)

# Plot forecast
plt.plot(forecast_df['date'], forecast_df['predicted_sales'], 
         label='Forecast', color='red', linewidth=2, marker='s', markersize=4)

# Plot confidence interval
plt.fill_between(forecast_df['date'], 
                 forecast_df['lower_bound'], 
                 forecast_df['upper_bound'], 
                 alpha=0.2, color='gray', label='85% Confidence Interval')

plt.title('Superstore Sales Forecast - Next 30 Days', fontsize=16, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot
plot_path = 'outputs/forecast_plot.png'
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"\n📈 Forecast plot saved to: {plot_path}")

# Show first few rows of forecast
print("\n📋 First 5 days of forecast:")
print(forecast_df.head().to_string(index=False))

print("\n✅ Forecast generation complete!")
