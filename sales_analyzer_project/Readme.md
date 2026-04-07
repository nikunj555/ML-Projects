# 📊 Sales Intelligence Platform

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![Machine Learning](https://img.shields.io/badge/ML-RandomForest%20%7C%20SVM-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**An Enterprise-Grade ML-Powered Sales Analytics & Forecasting Platform**

[Features](#-features) • [Tech Stack](#-tech-stack) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [API Documentation](#-api-documentation)

</div>

---

## 🎯 Project Overview

The **Sales Intelligence Platform** is a comprehensive, production-ready machine learning application that empowers businesses with accurate sales forecasting, intelligent analytics, and data-driven decision-making capabilities. By leveraging both Random Forest and SVM algorithms, the platform provides reliable 30-day sales predictions with confidence intervals, enabling proactive inventory management, resource allocation, and strategic planning.

### 🎯 What It Does

| Capability | Description |
|------------|-------------|
| **Sales Forecasting** | Predicts daily sales for the next 30 days with 85-95% confidence intervals |
| **Performance Analytics** | Analyzes sales trends, patterns, and anomalies across different time periods |
| **Model Comparison** | Compares Random Forest vs SVM performance to identify the best model |
| **Customer Insights** | Segments customers and identifies purchasing patterns |
| **Interactive Visualizations** | Provides dynamic charts, heatmaps, and trend analyses |
| **API-First Design** | RESTful API for seamless integration with other systems |

### 🎯 Project Aim

> **"To democratize sales forecasting by providing an accessible, accurate, and actionable ML-powered platform that helps businesses of all sizes make data-driven decisions."**

**Key Objectives:**
- ✅ Provide 85%+ accurate 30-day sales forecasts
- ✅ Enable real-time analytics with interactive dashboards
- ✅ Offer model transparency through feature importance analysis
- ✅ Deliver enterprise-grade performance with simple setup
- ✅ Support both batch and real-time prediction scenarios

---

## 🚀 Features

### 📈 **Interactive Dashboard**
- Real-time sales performance metrics
- Dynamic date range filtering
- Day-of-week sales analysis
- Monthly performance heatmaps
- Trend line with 7-day moving average
- Key performance indicators (KPIs)

### 🔮 **ML-Powered Forecasting**
- 30-day sales predictions using Random Forest
- Alternative SVM-based forecasting
- 85-95% confidence intervals
- Visual forecast with growth rate analysis
- CSV export functionality
- Model switching capability

### 🤖 **Model Insights**
- Feature importance analysis (Top 10 features)
- Model performance metrics (MAE, RMSE, R²)
- Random Forest vs SVM comparison
- Prediction accuracy scatter plots
- Model architecture details
- Error analysis and visualization

### 🎯 **Customer Segmentation**
- High/Medium/Low value customer classification
- Purchase frequency analysis
- Discount impact assessment
- Segment-wise performance metrics

### 🔍 **Anomaly Detection**
- One-Class SVM for unusual pattern detection
- Automatic outlier identification
- Sales spike/drop detection
- Alert-ready anomaly flags

### ⚙️ **System Features**
- Light/Dark theme support
- Auto-refresh capability (30s intervals)
- Multi-format data export (CSV, JSON)
- Configurable confidence levels
- Date range presets

---

## 🛠️ Tech Stack

### **Backend Technologies**

| Technology | Version | Purpose |
|------------|---------|---------|
| **FastAPI** | 0.104+ | High-performance REST API framework |
| **Uvicorn** | 0.24+ | ASGI server for FastAPI |
| **Scikit-learn** | 1.3+ | Machine learning algorithms |
| **Pandas** | 2.1+ | Data manipulation and analysis |
| **NumPy** | 1.26+ | Numerical computing |
| **Joblib** | 1.3+ | Model serialization |

### **Frontend Technologies**

| Technology | Version | Purpose |
|------------|---------|---------|
| **Streamlit** | 1.28+ | Interactive web application framework |
| **Plotly** | 5.17+ | Interactive data visualization |
| **Matplotlib** | 3.8+ | Static visualizations |
| **Seaborn** | 0.13+ | Statistical visualizations |

### **ML Algorithms**

| Algorithm | Use Case | Key Parameters |
|-----------|----------|----------------|
| **Random Forest** | Sales Forecasting | n_estimators=200, max_depth=15 |
| **SVR (SVM)** | Alternative Forecasting | kernel='rbf', C=100, gamma='scale' |
| **One-Class SVM** | Anomaly Detection | nu=0.1, kernel='rbf' |
| **SVC** | Customer Segmentation | kernel='rbf', probability=True |

### **Development Tools**

| Tool | Purpose |
|------|---------|
| **Git** | Version control |
| **PowerShell** | Command-line interface |
| **VS Code** | Development environment |
| **Postman** | API testing |

---

## 📊 Model Performance

### **Random Forest Regressor**

## 📊 Model Architecture

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         SALES INTELLIGENCE PLATFORM                                   │
│                              SYSTEM ARCHITECTURE                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            PRESENTATION LAYER                                         │
├───────────────┬───────────────┬───────────────┬───────────────┬─────────────────────┤
│   📈 Dashboard │  🔮 Forecast   │  🤖 Insights   │  ⚙️ Settings   │  📊 Comparison      │
│               │               │               │               │                     │
│ • Sales KPIs  │ • 30-day pred │ • Feature     │ • Theme       │ • RF vs SVM         │
│ • Trend lines │ • Confidence  │   importance  │ • API config  │ • Performance       │
│ • Heatmaps    │   intervals   │ • Model       │ • Data refresh│ • Error analysis    │
│ • Day analysis│ • CSV export  │   metrics     │               │                     │
└───────────────┴───────────────┴───────────────┴───────────────┴─────────────────────┘
                                      │
                                      │ HTTP/REST API
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              API GATEWAY LAYER                                        │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                           FastAPI Application                                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │  /health     │  │  /forecast   │  │  /models     │  │  /docs       │           │
│  │  GET         │  │  GET         │  │  GET         │  │  GET         │           │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘           │
│                                                                                     │
│  Middleware: CORS • Logging • Error Handling • Request Validation                   │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            BUSINESS LOGIC LAYER                                      │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │                         MODEL ORCHESTRATOR                                    │   │
│  │  ┌─────────────────────┐    ┌─────────────────────┐                         │   │
│  │  │   Random Forest     │    │        SVM          │                         │   │
│  │  │    Regressor        │    │    Regressor        │                         │   │
│  │  │                     │    │                     │                         │   │
│  │  │ • n_estimators=200  │    │ • kernel='rbf'      │                         │   │
│  │  │ • max_depth=15      │    │ • C=100             │                         │   │
│  │  │ • random_state=42   │    │ • gamma='scale'     │                         │   │
│  │  └─────────────────────┘    └─────────────────────┘                         │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │                      FEATURE ENGINEERING PIPELINE                            │   │
│  │                                                                              │   │
│  │  Raw Data ──► [Time Features] ──► [Lag Features] ──► [Rolling Windows]      │   │
│  │                    │                  │                    │                 │   │
│  │                    ▼                  ▼                    ▼                 │   │
│  │              day_of_week         sales_lag_1          sales_rolling_7        │   │
│  │              month               sales_lag_7          sales_rolling_30       │   │
│  │              year                sales_lag_30                                │   │
│  │              is_weekend                                                     │   │
│  │              is_holiday_season                                              │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                DATA LAYER                                            │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐        │
│  │   Raw Data    │  │  Processed    │  │    Models     │  │   Outputs     │        │
│  │               │  │    Data       │  │               │  │               │        │
│  │ • CSV files   │  │ • sales_data  │  │ • RF model    │  │ • Charts PNG  │        │
│  │ • Superstore  │  │   .csv        │  │ • SVM model   │  │ • CSV exports │        │
│  │   dataset     │  │               │  │ • Scaler.pkl  │  │ • Metrics     │        │
│  │               │  │               │  │ • features    │  │   reports     │        │
│  │               │  │               │  │   .json       │  │               │        │
│  └───────────────┘  └───────────────┘  └───────────────┘  └───────────────┘        │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              DATA FLOW DIAGRAM                                       │
└─────────────────────────────────────────────────────────────────────────────────────┘

Phase 1: DATA INGESTION
┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────┐
│  Raw CSV   │───►│  Validate  │───►│   Clean    │───►│   Ready    │
│  Files     │    │   Data     │    │   Data     │    │  DataFrame │
└────────────┘    └────────────┘    └────────────┘    └────────────┘

Phase 2: FEATURE ENGINEERING
┌────────────┐    ┌────────────┐    ┌────────────┐
│   Time     │───►│    Lag     │───►│  Rolling   │
│  Features  │    │  Features  │    │  Windows   │
└────────────┘    └────────────┘    └────────────┘

Phase 3: MODEL TRAINING
┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────┐
│  Train/    │───►│  Random    │───►│    SVM     │───►│   Model    │
│  Test Split│    │  Forest    │    │  Training  │    │   Save     │
│   (80/20)  │    │  Training  │    │            │    │            │
└────────────┘    └────────────┘    └────────────┘    └────────────┘

Phase 4: PREDICTION
┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────┐
│  Future    │───►│  Feature   │───►│   Model    │───►│ Confidence │
│   Dates    │    │  Creation  │    │  Predict   │    │  Interval  │
│   (30d)    │    │            │    │            │    │  (85-95%)  │
└────────────┘    └────────────┘    └────────────┘    └────────────┘


┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          DEPLOYMENT ARCHITECTURE                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          DEVELOPMENT ENVIRONMENT                                     │
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │                          LOCAL MACHINE                                       │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                      │   │
│  │  │   VS Code    │  │    Git       │  │   Python     │                      │   │
│  │  │     IDE      │  │   Repository │  │    3.8+      │                      │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘                      │   │
│  │                                                                              │   │
│  │  ┌──────────────────────────────────────────────────────────────────────┐  │   │
│  │  │                    Virtual Environment (venv)                         │  │   │
│  │  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐     │  │   │
│  │  │  │  Backend   │  │  Frontend  │  │   Models   │  │   Data    │     │  │   │
│  │  │  │  :8000     │  │  :8501     │  │   Store    │  │   Store   │     │  │   │
│  │  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘     │  │   │
│  │  └──────────────────────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          REQUEST-RESPONSE FLOW                                       │
└─────────────────────────────────────────────────────────────────────────────────────┘

  User ──► Streamlit ──► HTTP Request ──► FastAPI ──► Model ──► Prediction
   │         App           (JSON)         Backend     Loaded      Generated
   │                                                                      │
   │                                                                      │
   └──────────────────────────────────────────────────────────────────────┘
                              Response (JSON)


┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          TECHNOLOGY STACK FLOWCHART                                   │
└─────────────────────────────────────────────────────────────────────────────────────┘

                                    ┌─────────────────┐
                                    │     USER        │
                                    │   (Browser)     │
                                    └────────┬────────┘
                                             │
                                    ┌────────▼────────┐
                                    │   Streamlit     │
                                    │   Frontend      │
                                    │   Port :8501    │
                                    └────────┬────────┘
                                             │ HTTP
                                    ┌────────▼────────┐
                                    │   FastAPI       │
                                    │   Backend       │
                                    │   Port :8000    │
                                    └────────┬────────┘
                                             │
                    ┌────────────────────────┼────────────────────────┐
                    │                        │                        │
            ┌───────▼───────┐        ┌───────▼───────┐        ┌───────▼───────┐
            │   Random      │        │     SVM       │        │   Scaler      │
            │   Forest      │        │   Model       │        │   (if SVM)    │
            │   Model       │        │               │        │               │
            └───────────────┘        └───────────────┘        └───────────────┘
                    │                        │                        │
                    └────────────────────────┼────────────────────────┘
                                             │
                                    ┌────────▼────────┐
                                    │   Prediction    │
                                    │   Response      │
                                    │   (JSON/CSV)    │
                                    └─────────────────┘
