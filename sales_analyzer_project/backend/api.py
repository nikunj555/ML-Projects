# backend/api.py - FIXED VERSION
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel
from typing import List, Dict, Optional
import os
from datetime import datetime, timedelta
import json

# Initialize FastAPI app
app = FastAPI(
    title="Sales Prediction API",
    description="ML-powered sales forecasting system",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "sales_model.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "..", "models", "feature_cols.json")
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "sales_data.csv")

# Global variables
model = None
feature_cols = []
df = None
latest_data = None

@app.on_event("startup")
async def load_model():
    global model, feature_cols, df, latest_data
    
    print("\n" + "="*60)
    print("🚀 LOADING MODEL AND DATA")
    print("="*60)
    
    try:
        # Load feature columns FIRST
        if os.path.exists(FEATURES_PATH):
            with open(FEATURES_PATH, 'r') as f:
                feature_cols = json.load(f)
            print(f"✅ Features loaded: {len(feature_cols)} features")
            print(f"   Features: {feature_cols}")
        
        # Load model
        if os.path.exists(MODEL_PATH):
            model = joblib.load(MODEL_PATH)
            print(f"✅ Model loaded from {MODEL_PATH}")
            
            # Verify feature count matches
            if hasattr(model, 'n_features_in_'):
                print(f"   Model expects {model.n_features_in_} features")
                if len(feature_cols) != model.n_features_in_:
                    print(f"⚠️ WARNING: Feature count mismatch!")
        
        # Load latest data
        if os.path.exists(DATA_PATH):
            df = pd.read_csv(DATA_PATH)
            df['date'] = pd.to_datetime(df['date'])
            df = df.sort_values('date').reset_index(drop=True)
            latest_data = df.tail(60).copy()
            print(f"✅ Data loaded: {len(df)} days")
            print(f"   Date range: {df['date'].min()} to {df['date'].max()}")
        else:
            print("⚠️ Data file not found")
            
    except Exception as e:
        print(f"❌ Error loading: {e}")

# Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "features_loaded": len(feature_cols) > 0,
        "data_loaded": df is not None,
        "feature_count": len(feature_cols) if feature_cols else 0,
        "data_days": len(df) if df is not None else 0
    }

# 30-day forecast endpoint - FIXED VERSION
@app.get("/forecast/30day")
async def forecast_30day():
    """Generate 30-day forecast using latest data"""
    
    if model is None or df is None:
        raise HTTPException(status_code=503, detail="Model or data not loaded")
    
    if not feature_cols:
        raise HTTPException(status_code=503, detail="Feature list not loaded")
    
    try:
        # Generate future dates
        last_date = df['date'].max()
        future_dates = [last_date + timedelta(days=i+1) for i in range(30)]
        
        # Get latest data
        latest = df.tail(60).copy()
        
        # Make predictions
        predictions = []
        for i, date in enumerate(future_dates):
            # Create a dictionary with ALL features the model expects
            features = {}
            
            # Fill with appropriate values for each feature
            for col in feature_cols:
                if col == 'day_of_week':
                    features[col] = date.weekday()
                elif col == 'month':
                    features[col] = date.month
                elif col == 'year':
                    features[col] = date.year
                elif col == 'is_weekend':
                    features[col] = 1 if date.weekday() >= 5 else 0
                elif col == 'is_holiday_season':
                    features[col] = 1 if date.month in [11, 12] else 0
                elif col == 'discount':
                    features[col] = float(latest['discount'].mean())
                elif col == 'customers':
                    features[col] = int(latest['customers'].mean())
                elif col == 'quantity':
                    features[col] = int(latest['quantity'].mean())
                elif col == 'sales_lag_1':
                    if i == 0:
                        features[col] = float(latest['sales'].iloc[-1])
                    else:
                        features[col] = float(predictions[i-1])
                elif col == 'sales_lag_7':
                    if i < 7:
                        features[col] = float(latest['sales'].iloc[-7 + i])
                    else:
                        features[col] = float(predictions[i-7])
                elif col == 'sales_lag_30':
                    if i < 30:
                        features[col] = float(latest['sales'].iloc[-30 + i])
                    else:
                        features[col] = float(predictions[i-30])
                elif col == 'sales_rolling_7':
                    if i == 0:
                        features[col] = float(latest['sales'].iloc[-7:].mean())
                    else:
                        # Combine historical and predicted
                        hist_part = latest['sales'].iloc[-(7-i):].tolist() if i < 7 else []
                        pred_part = predictions[max(0, i-7):i]
                        combined = hist_part + pred_part
                        features[col] = float(np.mean(combined)) if combined else 0.0
                elif col == 'sales_rolling_30':
                    if i == 0:
                        features[col] = float(latest['sales'].tail(30).mean())
                    else:
                        hist_part = latest['sales'].iloc[-(30-i):].tolist() if i < 30 else []
                        pred_part = predictions[max(0, i-30):i]
                        combined = hist_part + pred_part
                        features[col] = float(np.mean(combined)) if combined else 0.0
                else:
                    # Default value for any other features
                    features[col] = 0.0
            
            # Create DataFrame with EXACT feature order
            features_df = pd.DataFrame([features])[feature_cols]
            
            # Predict
            pred = float(model.predict(features_df)[0])
            predictions.append(pred)
        
        # Calculate bounds
        lower_bounds = [p * 0.85 for p in predictions]
        upper_bounds = [p * 1.15 for p in predictions]
        
        return {
            "dates": [d.strftime('%Y-%m-%d') for d in future_dates],
            "predictions": predictions,
            "lower_bounds": lower_bounds,
            "upper_bounds": upper_bounds,
            "total": float(sum(predictions)),
            "average": float(np.mean(predictions))
        }
        
    except Exception as e:
        import traceback
        print(f"❌ Error in forecast: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

# Model info endpoint
@app.get("/model/info")
def model_info():
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    return {
        "model_type": type(model).__name__,
        "features": feature_cols,
        "n_features": len(feature_cols),
        "n_estimators": getattr(model, 'n_estimators', None),
        "max_depth": getattr(model, 'max_depth', None)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)