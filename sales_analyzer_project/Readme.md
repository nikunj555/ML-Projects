# ⚡ NeuralSales — AI-Powered Sales Forecast Intelligence Platform

NeuralSales is an advanced end-to-end Machine Learning powered sales forecasting and analytics platform built using:

- Streamlit
- FastAPI
- Scikit-learn
- XGBoost
- SHAP Explainability
- Plotly
- Pandas
- NumPy

The project combines:
- predictive analytics
- supervised machine learning
- explainable AI
- interactive dashboards
- model comparison
- forecasting intelligence

into a production-style ML analytics platform.

---

# 🚀 Features

## 📈 Advanced Sales Dashboard
- Interactive sales analytics
- KPI cards
- Revenue tracking
- Customer insights
- Trend analysis
- Moving averages
- Bollinger bands
- Monthly heatmaps
- Correlation analysis

---

## 🔮 30-Day AI Forecasting
Machine learning powered future sales forecasting with:
- confidence intervals
- upper/lower prediction bounds
- trend analysis
- growth rate visualization
- peak demand detection

---

## 🤖 Multi-Model ML Training Pipeline

The platform trains and compares multiple supervised ML models:

| Model | Type |
|---|---|
| Linear Regression | Linear Model |
| Lasso Regression | Regularized Linear |
| Ridge Regression | Regularized Linear |
| Decision Tree | Tree-Based |
| Random Forest | Ensemble Bagging |
| Gradient Boosting | Boosting |
| AdaBoost | Ensemble Boosting |
| Extra Trees | Randomized Ensemble |
| SVR | Kernel-Based |
| XGBoost | Advanced Gradient Boosting |

---

## 📊 Model Comparison Engine
Dynamic backend-powered model comparison dashboard:
- R² comparison
- RMSE analysis
- MAE analysis
- Accuracy metrics
- Cross-validation scores
- Best model selection

---

## 🧠 Explainable AI (XAI)
Integrated SHAP Explainability:
- feature importance analysis
- model interpretability
- prediction reasoning
- transparent ML decisions

---

## ⚙️ FastAPI Backend
Production-style backend architecture:
- REST APIs
- ML inference engine
- dynamic forecasting
- model serving
- health monitoring
- JSON endpoints

---

## 🎨 Premium Dark UI
Custom enterprise-grade UI featuring:
- futuristic dark theme
- neon cyber aesthetics
- interactive Plotly charts
- animated KPI cards
- responsive layout
- professional dashboard design

---

# 🧠 Machine Learning Concepts Used

This project demonstrates practical implementation of:

- Supervised Learning
- Regression Models
- Ensemble Learning
- Boosting Algorithms
- Regularization
- Time Series Forecasting
- Cross Validation
- Feature Engineering
- Explainable AI
- Model Evaluation
- Residual Analysis
- Bias-Variance Tradeoff
- Forecast Confidence Intervals

---

# 📂 Project Structure

```bash
sales_analyzer_project/
│
├── backend/
│   └── api.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── sales_data.csv
│
├── models/
│   ├── sales_model.pkl
│   ├── feature_cols.json
│   └── model_results.pkl
│
├── outputs/
│   ├── feature_importance.png
│   ├── actual_vs_predicted.png
│   └── residual_distribution.png
│
├── train_model.py
│
└── README.md
```

---

# ⚡ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/neuralsales.git

cd neuralsales
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows
```bash
venv\Scripts\activate
```

### Linux/Mac
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

---

## 1️⃣ Train Models

```bash
python train_model.py
```

This generates:

```bash
models/sales_model.pkl
models/model_results.pkl
models/feature_cols.json
```

---

## 2️⃣ Start Backend

```bash
cd backend

uvicorn api:app --reload
```

Backend runs at:

```bash
http://localhost:8000
```

---

## 3️⃣ Start Frontend

Open another terminal:

```bash
cd frontend

streamlit run app.py
```

Frontend runs at:

```bash
http://localhost:8501
```

---

# 📡 API Endpoints

| Endpoint | Description |
|---|---|
| `/health` | Backend health check |
| `/forecast/30day` | 30-day ML forecast |
| `/model/info` | Model metadata |
| `/model-comparison` | Dynamic model comparison |
| `/model/shap` | Explainable AI insights |

---

# 📊 Evaluation Metrics

The platform evaluates models using:

- MAE
- RMSE
- R² Score
- Cross Validation
- Forecast Accuracy

---

# 🧠 Explainable AI

SHAP analysis helps visualize:
- feature contributions
- prediction drivers
- model reasoning
- feature importance ranking

---

# 📈 Visualization Stack

- Plotly
- Plotly Graph Objects
- Plotly Express
- Matplotlib
- Seaborn

---

# 🔥 Advanced Highlights

✅ Dynamic ML Model Comparison  
✅ Production-style Backend APIs  
✅ Explainable AI Integration  
✅ Forecast Confidence Bands  
✅ Real-time Forecast Visualization  
✅ Advanced Ensemble Models  
✅ Enterprise Dashboard UI  
✅ Time-Series Aware Validation  
✅ Feature Engineering Pipeline  
✅ Cross Validation System  

---

# 🛠 Tech Stack

## Frontend
- Streamlit
- Plotly
- HTML/CSS

## Backend
- FastAPI
- Uvicorn

## ML & Data
- Scikit-learn
- XGBoost
- SHAP
- Pandas
- NumPy

---

# 📸 Screenshots

Add screenshots here:
- Dashboard
- Forecast Page
- Model Comparison
- Explainable AI
- Model Insights

---

# 🚀 Future Improvements

- LightGBM integration
- CatBoost integration
- Real-time streaming forecasts
- Authentication system
- Docker deployment
- Cloud deployment
- CI/CD pipeline
- Auto retraining
- Hyperparameter optimization
- Drift detection

---

# 👨‍💻 Author

Nikunj Katta

---

# ⭐ If you like this project

Give it a star on GitHub ⭐
