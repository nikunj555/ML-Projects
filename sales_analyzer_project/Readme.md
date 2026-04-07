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

┌─────────────────────────────────────────────────────────────────────────────┐
│                      SALES INTELLIGENCE PLATFORM                             │
│                          SYSTEM ARCHITECTURE                                 │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                       (Streamlit - Port 8501)                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│ │Dashboard │ │ Forecast │ │ Insights │ │ Settings │ │Comparison│            │ 
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘            │ 
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│ │ Sales KPIs│ │30d Predict│ │ Feature  │ │ RF vs SVM│ │Trend Lines│         │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘            │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│ │Confidence│ │ Heatmaps │ │Error Anal│ │ Day Anal │ │ CSV Export│           │
│ │Intervals │ │          │ │   ysis   │ │   ysis   │ │          │            │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘            │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      │ HTTP / REST API (JSON)
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         API GATEWAY LAYER                                   │
│                         (FastAPI - Port 8000)                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                    Request → Validate → Route → Response                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                             DATA LAYER                                      │
├─────────────────────────┬─────────────────────────┬─────────────────────────┤
│       RAW DATA          │     PROCESSED DATA      │     MODEL OUTPUTS       │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ • sales_data.csv        │ • Cleaned DataFrame     │ • SVM_model.pkl         │
│ • Superstore.csv        │ • Feature Engineered    │ • RandomForest_model.pkl│
│ • dataset/              │ • Train/Test (80/20)    │ • scaler.pkl            │
│                         │                         │                         │
│                         │                         │ • Charts (PNG)          │
│                         │                         │ • Metrics JSON          │
│                         │                         │ • CSV Exports           │
└─────────────────────────┴─────────────────────────┴─────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                           DATA FLOW DIAGRAM                                 │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   PHASE 1   │    │   PHASE 2   │    │   PHASE 3   │    │   PHASE 4   │
│DATA INGESTION│ → │  FEATURE    │ →  │   MODEL     │ →  │ PREDICTION  │
│             │    │ ENGINEERING │    │  TRAINING   │    │             │
├─────────────┤    ├─────────────┤    ├─────────────┤    ├─────────────┤
│ • Validate  │    │ • Time      │    │ • 80/20     │    │ • Predict   │
│ • Clean     │    │   Features  │    │   Split     │    │   30 Days   │
│ • Ready     │    │ • Lag       │    │ • Random    │    │ • Confidence│
│   DataFrame │    │   Features  │    │   Forest    │    │  Intervals  │
│             │    │ • Rolling   │    │ • SVM       │    │   (85-95%)  │
│             │    │   Windows   │    │ • Save .pkl │    │ • Future    │
│             │    │             │    │             │    │   Features  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         DEPLOYMENT ARCHITECTURE                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────┐      ┌─────────────────┐      ┌─────────────────┐
│          │      │                 │      │                 │
│   USER   │ ───► │   Streamlit     │ ───► │   FastAPI       │
│ (Browser)│      │   (Port 8501)   │      │   (Port 8000)   │
│          │      │                 │      │                 │
└──────────┘      └─────────────────┘      └────────┬────────┘
                                                     │
                                                     ▼
                              ┌─────────────────────────────────┐
                              │                                 │
                              │      Loaded Model (.pkl)        │
                              │                                 │
                              │         Prediction              │
                              │                                 │
                              └────────────────┬────────────────┘
                                               │
                                               ▼
                              ┌─────────────────────────────────┐
                              │                                 │
                              │       JSON Response             │
                              │                                 │
                              └─────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         TECHNOLOGY STACK FLOWCHART                          │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  USER    │      │  Streamlit   │      │   FastAPI    │      │   Model      │
│          │ ───► │  Frontend    │ ───► │   Backend    │ ───► │   Loaded     │
│ (Browser)│      │  :8501       │      │   :8000      │      │   (.pkl)     │
└──────────┘      └──────────────┘      └──────┬───────┘      └──────┬───────┘
                                               │                     │
                                               │ ◄───────────────────┘
                                               ▼
                                      ┌──────────────┐
                                      │  Prediction  │
                                      │  + JSON      │
                                      │  Response    │
                                      └──────────────┘        
