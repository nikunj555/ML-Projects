# 🚀 Sales Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green?style=flat-square&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.3-red?style=flat-square&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-orange?style=flat-square&logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

> **An Enterprise-Grade ML-Powered Sales Analytics & Forecasting Platform**

[Features](#features) • [Demo](#demo) • [Architecture](#architecture) • [ML Model](#ml-model) • [Tech Stack](#tech-stack) • [Installation](#installation) • [API Docs](#api-docs)

---

## 📌 Project Overview

The **Sales Intelligence Platform** is a comprehensive, production-ready machine learning application for sales forecasting and analytics. It provides accurate 30-day sales predictions with confidence intervals, enabling proactive inventory management, resource allocation, and strategic planning. By leveraging both traditional time-series and SVM algorithms, the platform provides reliable 30-day sales predictions with confidence metrics, enabling proactive inventory management, resource allocation, and strategy planning.

---

## 💡 What It Does

| Capability | Description |
|---|---|
| **Sales Forecasting** | Predicts daily sales for the next 30 days with 95% confidence intervals |
| **Performance Analytics** | Analyses sales trends, patterns, and anomalies across different time periods |
| **Model Comparison** | Compares Random Forest vs SVM performance to identify the best model |
| **Customer Insights** | Segments customers and identifies purchasing patterns |
| **Interactive REST API** | Provides structured endpoints for storage, retrieval, and trend analysis |
| **API First Design** | RESTful API for seamless integration with other systems |

---

## 🎯 Project Aims

> *"To democratise sales forecasting by providing an accessible, accurate, and actionable ML-powered platform that helps businesses of all sizes make data-driven decisions."*

**Key Objectives:**
- ✅ Provide 85%+ accurate 30-day sales forecasts
- ✅ Enable real-time analytics with interactive dashboards
- ✅ Ensure model transparency through feature importance analysis
- ✅ Deliver an enterprise-grade performance with simultaneous service
- ✅ Support both batch and real-time prediction scenarios

---

## ✨ Features

### 📊 Interactive Dashboard
- Key time-series performance metrics
- Dynamic data range filtering
- Cut-off point sales analysis
- Monthly performance heatmaps
- Head-to-head model comparison
- Key performance indicator (KPI) display

### 🤖 ML-Powered Forecasting
- 30-day sales predictions using Random Forest
- Alternative SVM-based forecasting
- 95–97% confidence intervals
- Hour-based with 7-day training average
- Model quality capability

### 🔍 Model Insights
- Feature importance analysis (top 10 features)
- Model performance metrics (MAE, RMSE, R²)
- Prediction accuracy scatter plots
- Validation accuracy scatter plots
- Model architecture details

### 👥 Customer Segmentation
- High/Medium/Low value customer classification
- Purchase frequency analysis
- Choice of impact assessment
- Segment-wise performance metrics

### 🚨 Anomaly Detection
- One-Class SVM for unusual pattern detection
- Multivariate data distribution
- Sales spiking detection
- Macroeconomic anomaly flags

### ⚙️ System Features
- Lightweight theme support
- Auto-refresh capability (30-second intervals)
- Multi-format data export (CSV, JSON)
- Configurable confidence intervals
- Date-range presets

---

## 🏗️ Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  SALES INTELLIGENCE PLATFORM                │
│                     SYSTEM ARCHITECTURE                     │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
   ┌──────────────────┐            ┌──────────────────────┐
   │  STREAMLIT UI    │            │     FASTAPI BACKEND  │
   │  (Port 8501)     │◄──REST────►│     (Port 8000)      │
   │                  │            │                      │
   │ • Dashboard      │            │ • /predict           │
   │ • Forecasts      │            │ • /forecast/30day    │
   │ • Insights       │            │ • /anomaly           │
   │ • Settings       │            │ • /segments          │
   │ • Comparison     │            │ • /health            │
   └──────────────────┘            └──────────┬───────────┘
                                              │
                    ┌─────────────────────────┤
                    ▼                         ▼
         ┌──────────────────┐      ┌──────────────────────┐
         │   ML ENGINE      │      │    DATA LAYER        │
         │                  │      │                      │
         │ • Random Forest  │      │ • Raw Sales Data     │
         │ • SVM Model      │      │ • Processed Features │
         │ • Anomaly Model  │      │ • Outputs/Cache      │
         │ • Scaler/Encoder │      │                      │
         └──────────────────┘      └──────────────────────┘
```

### Frontend Architecture

```
┌─────────────────────────────────────────────┐
│             STREAMLIT FRONTEND              │
└─────────────────────────────────────────────┘
                      │
    ┌─────────────────┼─────────────────┐
    ▼                 ▼                 ▼
┌────────┐      ┌──────────┐     ┌──────────┐
│ Pages  │      │Components│     │  Utils   │
│        │      │          │     │          │
│ Home   │      │ Charts   │     │ API Call │
│ Fore.  │      │ KPI Cards│     │ Day Anal │
│ Insights│     │ Filters  │     │ CSV Rpts │
└────────┘      └──────────┘     └──────────┘
```

### Backend Architecture

```
┌─────────────────────────────────────────────┐
│              FASTAPI BACKEND                │
└─────────────────────────────────────────────┘
                      │
    ┌─────────────────┼──────────────────┐
    ▼                 ▼                  ▼
┌─────────┐    ┌───────────┐     ┌──────────────┐
│ ROUTERS │    │ SERVICES  │     │   MODELS     │
│         │    │           │     │              │
│/predict │    │Forecast   │     │ Pydantic     │
│/forecast│    │Anomaly    │     │ Request &    │
│/segment │    │Segment    │     │ Response     │
│/health  │    │Analytics  │     │ Schemas      │
└─────────┘    └───────────┘     └──────────────┘
```

### Data Flow

```
RAW DATA
    │
    ▼
┌─────────────────┐
│ DATA INGESTION  │  ← CSV / API / Database
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  PREPROCESSING  │  ← Missing values, Outliers, Encoding
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│FEATURE ENGINEER.│  ← Lag features, Rolling avg, Seasonality
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  MODEL TRAINING │  ← Random Forest + SVM + One-Class SVM
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   PREDICTION    │  ← 30-day forecast + Confidence interval
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   VALIDATION    │  ← MAE, RMSE, R², Accuracy metrics
└────────┬────────┘
         │
    ┌────┴─────┐
    ▼          ▼
┌───────┐  ┌───────┐
│ CHAT  │  │ API   │
│  UI   │  │ JSON  │
└───────┘  └───────┘
```

---

## 🤖 ML Model

### Model Architecture

```
┌──────────────────────────────────────────────────┐
│           RANDOM FOREST REGRESSOR                │
│                                                  │
│  Input Features (15+)                            │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│  │   Lag    │ │ Rolling  │ │ Calendar │  ...     │
│  │ Features │ │   Avg    │ │ Features │         │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘         │
│       └────────────┼────────────┘               │
│                    ▼                             │
│         ┌──────────────────┐                    │
│         │  StandardScaler  │                    │
│         └────────┬─────────┘                    │
│                  │                              │
│    ┌─────────────┼─────────────┐               │
│    ▼             ▼             ▼               │
│ ┌──────┐     ┌──────┐     ┌──────┐            │
│ │Tree 1│     │Tree 2│     │Tree N│  n=100     │
│ └──┬───┘     └──┬───┘     └──┬───┘            │
│    └────────────┼────────────┘               │
│                 ▼                             │
│         ┌─────────────┐                      │
│         │  Averaging  │  (Ensemble Output)   │
│         └──────┬──────┘                      │
│                ▼                             │
│   ┌─────────────────────────┐               │
│   │  Sales Prediction +     │               │
│   │  Confidence Interval    │               │
│   └─────────────────────────┘               │
└──────────────────────────────────────────────┘
```

### Model Performance Metrics

| Metric | Random Forest | SVM |
|--------|--------------|-----|
| **MAE** | Low | Medium |
| **RMSE** | Low | Medium |
| **R² Score** | ~0.87+ | Variable |
| **Accuracy** | ~87% | ~82% |
| **Confidence** | 95–97% | 90–94% |

### Feature Engineering

```
Raw Date Column
      │
      ├──► Day of Week      (0–6)
      ├──► Month            (1–12)
      ├──► Quarter          (1–4)
      ├──► Is Weekend       (0/1)
      ├──► Lag 1 day        (yesterday's sales)
      ├──► Lag 7 days       (last week same day)
      ├──► Lag 30 days      (last month same day)
      ├──► Rolling Mean 7   (7-day average)
      ├──► Rolling Mean 30  (30-day average)
      └──► Rolling Std 7    (7-day volatility)
```

---

## 🛠️ Tech Stack

### Backend Technologies

| Technology | Version | Purpose |
|---|---|---|
| **FastAPI** | 0.104+ | High-performance REST API framework |
| **Uvicorn** | 0.24+ | ASGI server for FastAPI |
| **Scikit-learn** | 1.3+ | Machine learning algorithms |
| **NumPy** | 1.24+ | Numerical data manipulation |
| **Joblib** | 1.3+ | Model serialisation |

### Frontend Technologies

| Technology | Version | Purpose |
|---|---|---|
| **Streamlit** | 1.3+ | Interactive web application framework |
| **Plotly** | 5.17+ | Interactive data visualisation |
| **Matplotlib** | 3.8+ | Static data visualisation |
| **SciPy** | 1.11+ | Statistical visualisations |

### ML Algorithms

| Algorithm | Use Case | Key Parameters |
|---|---|---|
| **Random Forest** | Sales forecasting | n_estimators=100, max_depth=15 |
| **Linear SVM** | Alternative forecasting | kernel=linear, gamma=scale |
| **One-Class SVM** | Anomaly detection | kernel=rbf, nu=0.1, gamma=0.1 |
| **SVC** | Customer segmentation | kernel=rbf, probability=True |

### Development Tools

| Tool | Purpose |
|---|---|
| **Git** | Version control |
| **PowerShell** | Command-line interface |
| **VS Code** | Development environment |
| **Pytest** | API testing |

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/nikunj555/sales-intelligence-platform.git
cd sales-intelligence-platform

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the FastAPI backend
uvicorn app.main:app --reload --port 8000

# 5. Run the Streamlit frontend (new terminal)
streamlit run streamlit_app.py
```

---

## 📡 API Docs

Once the server is running, visit:

```
Swagger UI  →  http://localhost:8000/docs
ReDoc       →  http://localhost:8000/redoc
```

### Key Endpoints

```
POST  /predict              →  Single prediction
GET   /forecast/30day       →  30-day forecast with confidence
GET   /anomaly              →  Anomaly detection results
GET   /segments             →  Customer segmentation
GET   /health               →  API health check
```

---

## 📁 Project Structure

```
sales-intelligence-platform/
│
├── app/
│   ├── main.py                  # FastAPI app entry point
│   ├── routers/
│   │   ├── predict.py
│   │   ├── forecast.py
│   │   ├── anomaly.py
│   │   └── segments.py
│   ├── services/
│   │   ├── forecast_service.py
│   │   ├── anomaly_service.py
│   │   └── segment_service.py
│   └── models/
│       └── schemas.py
│
├── ml/
│   ├── train.py                 # Model training script
│   ├── features.py              # Feature engineering
│   └── saved_models/            # Serialised .pkl files
│
├── streamlit_app.py             # Frontend entry point
├── requirements.txt
└── README.md
```

---

## 📊 Model Performance

The Random Forest model consistently outperforms SVM for this time-series sales forecasting task:

- **~87% forecasting accuracy** on test data
- **95–97% confidence intervals** on 30-day predictions
- **Low MAE & RMSE** compared to baseline models
- **Robust to outliers** due to ensemble averaging

---

