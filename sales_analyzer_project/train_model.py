import pandas as pd
import numpy as np
import os
import json
import joblib

from sklearn.model_selection import cross_val_score, TimeSeriesSplit
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ================= LINEAR MODELS =================

from sklearn.linear_model import (
    LinearRegression,
    Lasso,
    Ridge
)

# ================= TREE MODELS =================

from sklearn.tree import DecisionTreeRegressor

# ================= ENSEMBLE MODELS =================

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor,
    ExtraTreesRegressor
)

# ================= SUPPORT VECTOR =================

from sklearn.svm import SVR

# ================= XGBOOST =================

from xgboost import XGBRegressor

# ================= VISUALIZATION =================

import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 70)
print("🧠 ADVANCED SALES FORECAST MODEL TRAINING")
print("=" * 70)

# =========================================================
# CREATE DIRECTORIES
# =========================================================

os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# =========================================================
# LOAD DATA
# =========================================================

print("\n📂 Loading dataset...")

df = pd.read_csv("data/sales_data.csv")

df["date"] = pd.to_datetime(df["date"])

print(f"✅ Dataset Loaded Successfully")
print(f"📊 Total Records: {len(df)}")

# =========================================================
# FEATURE SELECTION
# =========================================================

feature_cols = [

    "day_of_week",
    "month",
    "year",
    "is_weekend",
    "is_holiday_season",

    "discount",
    "customers",
    "quantity",

    "sales_lag_1",
    "sales_lag_7",
    "sales_lag_30",

    "sales_rolling_7",
    "sales_rolling_30"
]

available_features = [
    col for col in feature_cols
    if col in df.columns
]

print(f"\n🔧 Using {len(available_features)} Features")

for feat in available_features:
    print(f"   • {feat}")

X = df[available_features]
y = df["sales"]

# =========================================================
# TRAIN TEST SPLIT
# =========================================================

train_size = int(len(df) * 0.8)

X_train = X[:train_size]
X_test = X[train_size:]

y_train = y[:train_size]
y_test = y[train_size:]

print("\n📊 Dataset Split")
print(f"Train Size : {len(X_train)}")
print(f"Test Size  : {len(X_test)}")

# =========================================================
# TIME SERIES CROSS VALIDATION
# =========================================================

tscv = TimeSeriesSplit(n_splits=5)

# =========================================================
# MODELS
# =========================================================

models = {

    "Linear Regression": LinearRegression(),

    "Lasso Regression": Lasso(
        alpha=0.1
    ),

    "Ridge Regression": Ridge(
        alpha=1.0
    ),

    "Decision Tree": DecisionTreeRegressor(
        max_depth=10,
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=200,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    ),

    "Gradient Boosting": GradientBoostingRegressor(
        random_state=42
    ),

    "AdaBoost": AdaBoostRegressor(
        random_state=42
    ),

    "Extra Trees": ExtraTreesRegressor(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    ),

    "SVR": SVR(
        kernel='rbf',
        C=100,
        gamma=0.1,
        epsilon=0.1
    ),

    "XGBoost": XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6,
        random_state=42
    )
}

# =========================================================
# TRAINING
# =========================================================

results = []

best_model = None
best_model_name = None
best_r2 = -999999

print("\n🚀 Training Models...\n")

for name, model in models.items():

    print(f"🔹 Training {name}...")

    try:

        # ================= TRAIN =================

        model.fit(X_train, y_train)

        # ================= PREDICT =================

        preds = model.predict(X_test)

        # ================= METRICS =================

        mae = mean_absolute_error(y_test, preds)

        rmse = np.sqrt(
            mean_squared_error(y_test, preds)
        )

        r2 = r2_score(y_test, preds)

        accuracy = 100 * (
            1 - (mae / y_test.mean())
        )

        # ================= CROSS VALIDATION =================

        cv_scores = cross_val_score(
            model,
            X,
            y,
            cv=tscv,
            scoring='r2'
        )

        cv_mean = cv_scores.mean()

        # ================= SAVE RESULTS =================

        results.append({

            "Model": name,

            "MAE": round(mae, 2),

            "RMSE": round(rmse, 2),

            "R2 Score": round(r2, 4),

            "Accuracy": round(accuracy, 2),

            "CV Mean": round(cv_mean, 4)
        })

        # ================= BEST MODEL =================

        if r2 > best_r2:

            best_r2 = r2

            best_model = model

            best_model_name = name

        print(f"   ✅ MAE       : {mae:.2f}")
        print(f"   ✅ RMSE      : {rmse:.2f}")
        print(f"   ✅ R² Score  : {r2:.4f}")
        print(f"   ✅ Accuracy  : {accuracy:.2f}%")
        print(f"   ✅ CV Mean   : {cv_mean:.4f}")

        print("-" * 50)

    except Exception as e:

        print(f"❌ Error training {name}: {e}")

# =========================================================
# RESULTS DATAFRAME
# =========================================================

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="R2 Score",
    ascending=False
)

print("\n🏆 MODEL COMPARISON RESULTS")
print("=" * 70)

print(results_df.to_string(index=False))

# =========================================================
# SAVE MODEL RESULTS
# =========================================================

joblib.dump(
    results_df,
    "models/model_results.pkl"
)

print("\n💾 models/model_results.pkl saved")

# =========================================================
# SAVE BEST MODEL
# =========================================================

joblib.dump(
    best_model,
    "models/sales_model.pkl"
)

print("💾 models/sales_model.pkl saved")

# =========================================================
# SAVE FEATURES
# =========================================================

with open(
    "models/feature_cols.json",
    "w"
) as f:

    json.dump(
        available_features,
        f
    )

print("💾 models/feature_cols.json saved")

# =========================================================
# FEATURE IMPORTANCE
# =========================================================

if hasattr(best_model, "feature_importances_"):

    importance_df = pd.DataFrame({

        "Feature": available_features,

        "Importance": best_model.feature_importances_

    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    print("\n🔑 FEATURE IMPORTANCE")
    print("=" * 70)

    print(
        importance_df.to_string(index=False)
    )

    # ================= PLOT =================

    plt.figure(figsize=(12, 6))

    sns.barplot(
        data=importance_df,
        x="Importance",
        y="Feature"
    )

    plt.title(
        f"Feature Importance - {best_model_name}"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/feature_importance.png",
        dpi=150
    )

    plt.close()

    print("\n📊 outputs/feature_importance.png saved")

# =========================================================
# ACTUAL VS PREDICTED
# =========================================================

final_preds = best_model.predict(X_test)

plt.figure(figsize=(10, 6))

plt.plot(
    y_test.values[:100],
    label="Actual Sales"
)

plt.plot(
    final_preds[:100],
    label="Predicted Sales"
)

plt.title(
    f"Actual vs Predicted - {best_model_name}"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "outputs/actual_vs_predicted.png",
    dpi=150
)

plt.close()

print("📈 outputs/actual_vs_predicted.png saved")

# =========================================================
# RESIDUAL ANALYSIS
# =========================================================

residuals = y_test.values - final_preds

plt.figure(figsize=(10, 6))

sns.histplot(
    residuals,
    bins=30,
    kde=True
)

plt.title(
    "Residual Distribution"
)

plt.tight_layout()

plt.savefig(
    "outputs/residual_distribution.png",
    dpi=150
)

plt.close()

print("📉 outputs/residual_distribution.png saved")

# =========================================================
# FINAL SUMMARY
# =========================================================

print("\n" + "=" * 70)

print("✅ TRAINING COMPLETED SUCCESSFULLY")

print("=" * 70)

print(f"\n🏆 BEST MODEL : {best_model_name}")

print(f"📊 BEST R²    : {best_r2:.4f}")

print("\n📁 Saved Files:")

print("   • models/sales_model.pkl")
print("   • models/model_results.pkl")
print("   • models/feature_cols.json")
print("   • outputs/feature_importance.png")
print("   • outputs/actual_vs_predicted.png")
print("   • outputs/residual_distribution.png")

print("\n🚀 Your ML pipeline is production-ready.")
