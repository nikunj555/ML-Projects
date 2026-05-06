⚡ NeuralSales · Forecast Intelligence










Premium ML-Powered Sales Forecasting & Analytics Dashboard

🚀 Project Overview

NeuralSales is an enterprise-style AI-powered sales analytics and forecasting platform built using:

Streamlit for the frontend dashboard
FastAPI for backend APIs
Scikit-learn for machine learning
Plotly for interactive visualizations

The platform provides:

✅ 30-Day sales forecasting
✅ Real-time ML analytics
✅ KPI dashboards
✅ Interactive visualizations
✅ Feature importance analysis
✅ Confidence interval forecasting
✅ Model insights & prediction accuracy analysis

✨ Core Features
📈 Interactive Dashboard

The dashboard provides:

Revenue trend analysis
Moving averages
Bollinger bands
Monthly sales heatmaps
Customer vs Sales analysis
Discount impact analytics
Dynamic KPI cards
Date-range filtering
KPIs Included
Total Revenue
Daily Average Revenue
Peak Sales Day
Customer Volume
🔮 ML Forecasting System
30-Day Forecast Engine

The forecasting engine predicts future sales using machine learning models with confidence intervals.

Forecast Includes
Daily predictions
Upper & lower confidence bounds
Growth-rate analytics
Peak-day detection
Risk analysis
Forecast export CSV
Visual Components
Forecast confidence bands
Growth percentage charts
Trend analysis cards
Forecast tables
🤖 Model Insights
ML Analytics Dashboard

The platform provides model explainability using:

Feature importance charts
MAE analysis
RMSE analysis
R² Score evaluation
Prediction accuracy scatter plots
Residual distribution analysis
Metrics Supported
Metric	Description
MAE	Mean Absolute Error
RMSE	Root Mean Squared Error
R² Score	Model accuracy score
Accuracy	Forecasting accuracy
⚙️ System Features
Backend Monitoring
Live backend status
Health monitoring
Model availability tracking
Auto backend detection
Data Export
Historical CSV export
Forecast CSV export
Configuration
Confidence interval controls
Backend URL configuration
Cache clearing
Model retraining triggers
🏗️ System Architecture
┌─────────────────────────────────────┐
│          NeuralSales UI             │
│          Streamlit Frontend         │
└─────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│          FastAPI Backend            │
│       Forecast Intelligence API     │
└─────────────────────────────────────┘
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
┌──────────────┐   ┌────────────────┐
│ ML Models    │   │ Sales Dataset  │
│ RandomForest │   │ Historical CSV │
│ Forecasting  │   │ Feature Store  │
└──────────────┘   └────────────────┘
📊 Frontend Features
Premium Dark Theme UI

The frontend includes:

Fully custom CSS theme
Premium neon UI
Animated KPI cards
Interactive Plotly charts
Responsive dashboard layout
Sidebar navigation
Modern enterprise dashboard design
Theme Colors
Element	Color
Primary Background	#080b12
Accent Cyan	#00d4ff
Emerald	#00e5a0
Violet	#8b5cf6
📡 Backend API Endpoints
Endpoint	Method	Description
/health	GET	Backend health status
/forecast/30day	GET	Generate 30-day forecast
/model/info	GET	ML model metadata
/model/retrain	POST	Trigger retraining
🤖 Machine Learning Pipeline
Forecasting Workflow
Historical Sales Data
        │
        ▼
Feature Engineering
        │
        ▼
Lag Features + Rolling Avg
        │
        ▼
Random Forest Regressor
        │
        ▼
30-Day Prediction
        │
        ▼
Confidence Interval Generation
        │
        ▼
Dashboard Visualization
🛠️ Tech Stack
Frontend
Technology	Purpose
Streamlit	Dashboard UI
Plotly	Interactive Charts
HTML/CSS	Custom Styling
Backend
Technology	Purpose
FastAPI	REST API
Uvicorn	ASGI Server
Requests	API Communication
Machine Learning
Technology	Purpose
Scikit-learn	Forecast Models
Pandas	Data Processing
NumPy	Numerical Operations
📁 Project Structure
sales_analyzer_project/
│
├── backend/
│   ├── api.py
│   ├── models/
│   └── services/
│
├── frontend/
│   └── app.py
│
├── data/
│   └── sales_data.csv
│
├── models/
│   ├── sales_model.pkl
│   └── feature_cols.json
│
└── README.md
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/neuralsales.git
cd neuralsales
2️⃣ Create Virtual Environment
python -m venv venv
Activate Environment
Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
🚀 Running the Project
Start Backend
cd backend

uvicorn api:app --reload --host 0.0.0.0 --port 8000
Start Frontend

Open another terminal:

cd frontend

streamlit run app.py
🌐 Application URLs
Service	URL
Frontend	http://localhost:8501

Backend API	http://localhost:8000

Swagger Docs	http://localhost:8000/docs
📊 Forecast Capabilities

The system provides:

✅ Sales trend forecasting
✅ Confidence interval estimation
✅ Growth-rate analysis
✅ Forecast risk analytics
✅ Interactive prediction visualization
✅ Feature-based prediction explainability

🎨 UI Highlights
Neon enterprise dashboard
Dark futuristic theme
Responsive analytics layout
Animated KPI system
Premium visual styling
Interactive charts
🔥 Future Enhancements
LSTM/Transformer forecasting
Real-time database integration
Multi-user authentication
Cloud deployment
Live streaming analytics
AI anomaly detection
Auto ML retraining
📜 License

MIT License

👨‍💻 Author

Nikunj Katta
AI/ML Developer · Data Analytics Enthusiast

⭐ Final Note

NeuralSales combines:

Modern frontend engineering
Real-time ML forecasting
Interactive analytics
Enterprise dashboard design

into a single intelligent sales forecasting platform.
