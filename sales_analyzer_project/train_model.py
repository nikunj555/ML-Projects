import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
import json
from sklearn.model_selection import TimeSeriesSplit

print("="*60)
print("🧠 MODEL TRAINING")
print("="*60)

# Create directories
os.makedirs('models', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

# Load data
print("\n📂 Loading Superstore data...")
df = pd.read_csv('data/sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
print(f"✅ Loaded {len(df)} days of data")

# Define features (columns that exist in our dataset)
feature_cols = [
    'day_of_week', 'month', 'year', 'is_weekend', 'is_holiday_season',
    'discount', 'customers', 'quantity',
    'sales_lag_1', 'sales_lag_7', 'sales_lag_30',
    'sales_rolling_7', 'sales_rolling_30'
]

# Check which features actually exist in the dataframe
available_features = [col for col in feature_cols if col in df.columns]
print(f"\n🔧 Using {len(available_features)} features: {available_features}")

X = df[available_features]
y = df['sales']

print(f"📊 Training samples: {len(X)}")

# Split data chronologically (respecting time series order)
train_size = int(len(df) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

print(f"\n📊 Train size: {len(X_train)} days")
print(f"   Test size: {len(X_test)} days")
print(f"   Train period: {df['date'].iloc[0]} to {df['date'].iloc[train_size-1]}")
print(f"   Test period: {df['date'].iloc[train_size]} to {df['date'].iloc[-1]}")

# Train Random Forest model
print("\n🎯 Training Random Forest...")
model = RandomForestRegressor(
    n_estimators=200,      # More trees for better accuracy
    max_depth=15,           # Allow deeper trees
    min_samples_split=5,    # Prevent overfitting
    min_samples_leaf=2,     # Smooth predictions
    random_state=42,
    n_jobs=-1,
    verbose=0
)

model.fit(X_train, y_train)

# Evaluate
print("\n📊 Evaluating model...")
y_pred = model.predict(X_test)

# Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
accuracy = 100 * (1 - mae / y_test.mean())

print(f"\n✅ Model Performance:")
print(f"   MAE: ${mae:,.2f}")
print(f"   RMSE: ${rmse:,.2f}")
print(f"   R² Score: {r2:.3f}")
print(f"   Accuracy: {accuracy:.1f}%")

# Feature Importance
importance = pd.DataFrame({
    'feature': available_features,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print("\n🔑 Top 5 Important Features:")
print(importance.head().to_string(index=False))

# Plot feature importance
plt.figure(figsize=(12, 6))
sns.barplot(data=importance.head(10), x='importance', y='feature')
plt.title('Top 10 Feature Importance - Superstore Data')
plt.tight_layout()
plt.savefig('outputs/feature_importance.png', dpi=150)
print(f"\n💾 Feature importance plot saved to outputs/feature_importance.png")

# Save model
model_path = 'models/sales_model.pkl'
joblib.dump(model, model_path)
print(f"💾 Model saved to: {model_path}")

# Save feature list (needed for API)
with open('models/feature_cols.json', 'w') as f:
    json.dump(available_features, f)
print(f"💾 Feature list saved to: models/feature_cols.json")

print("\n✅ Training complete!")