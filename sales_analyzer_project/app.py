import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import requests
import os
from datetime import datetime

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Sales Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
    <style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .status-online {
        background: #10b981;
        color: white;
        padding: 0.25rem 1rem;
        border-radius: 20px;
        display: inline-block;
    }
    .status-offline {
        background: #ef4444;
        color: white;
        padding: 0.25rem 1rem;
        border-radius: 20px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== FIND WORKING BACKEND ====================
def find_backend():
    """Find which backend URL works"""
    possible_urls = [
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ]
    
    for url in possible_urls:
        try:
            response = requests.get(f"{url}/health", timeout=2)
            if response.status_code == 200:
                return url, True
        except:
            continue
    return "http://127.0.0.1:8000", False

BACKEND_URL, BACKEND_AVAILABLE = find_backend()

# ==================== HEADER ====================
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.title("📊 Sales Intelligence Platform")
    st.markdown("ML-Powered Analytics & Forecasting")

with col2:
    if BACKEND_AVAILABLE:
        st.markdown(f"<div class='status-online'>✅ ML Backend: Online</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='status-offline'>❌ ML Backend: Offline</div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<small>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small>", unsafe_allow_html=True)

st.markdown("---")

# ==================== LOAD DATA ====================
@st.cache_data
def load_data():
    """Load historical data"""
    data_path = os.path.join('..', 'data', 'sales_data.csv')
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        df['date'] = pd.to_datetime(df['date'])
        return df
    return None

@st.cache_data(ttl=30)
def get_forecast():
    """Get forecast from backend"""
    if not BACKEND_AVAILABLE:
        return None
    try:
        response = requests.get(f"{BACKEND_URL}/forecast/30day", timeout=3)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None

df = load_data()
forecast_data = get_forecast()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.header("🎛️ Controls")
    
    # Date range filter
    if df is not None:
        min_date = df['date'].min().date()
        max_date = df['date'].max().date()
        date_range = st.date_input(
            "Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )
    else:
        date_range = (datetime(2022,1,1).date(), datetime(2023,12,31).date())
    
    st.markdown("---")
    st.info(
        "📊 **Data Source**\n"
        "Kaggle Superstore dataset\n"
        "📅 2+ years of transactions"
    )

# ==================== MAIN CONTENT ====================

# Dashboard Tab
st.header("📈 Performance Overview")

if df is not None:
    # Filter data
    if len(date_range) == 2:
        start_date, end_date = date_range
        mask = (df['date'].dt.date >= start_date) & (df['date'].dt.date <= end_date)
        filtered_df = df[mask]
    else:
        filtered_df = df
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_sales = filtered_df['sales'].sum()
        st.metric("Total Revenue", f"${total_sales:,.0f}")
    
    with col2:
        avg_daily = filtered_df['sales'].mean()
        st.metric("Avg Daily", f"${avg_daily:,.0f}")
    
    with col3:
        best_day = filtered_df.loc[filtered_df['sales'].idxmax()]
        st.metric("Best Day", best_day['date'].strftime('%Y-%m-%d'))
    
    with col4:
        total_customers = filtered_df['customers'].sum()
        st.metric("Total Customers", f"{total_customers:,.0f}")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.line(filtered_df, x='date', y='sales', title='Sales Trend')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        dow_sales = filtered_df.groupby('day_of_week')['sales'].mean().reset_index()
        fig2 = px.bar(dow_sales, x='day_of_week', y='sales', 
                     title='Avg Sales by Day',
                     labels={'day_of_week': 'Day (0=Mon, 6=Sun)'})
        st.plotly_chart(fig2, use_container_width=True)

else:
    st.warning("No historical data found. Please run fetch_superstore.py")

# Forecast Tab
st.markdown("---")
st.header("🔮 ML-Powered Forecast")

if BACKEND_AVAILABLE:
    if forecast_data:
        # Create forecast dataframe
        forecast_df = pd.DataFrame({
            'date': pd.to_datetime(forecast_data['dates']),
            'predicted': forecast_data['predictions'],
            'lower': forecast_data['lower_bounds'],
            'upper': forecast_data['upper_bounds']
        })
        
        # Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("30-Day Total", f"${forecast_data['total']:,.0f}")
        col2.metric("Daily Average", f"${forecast_data['average']:,.0f}")
        col3.metric("Peak Day", f"${max(forecast_data['predictions']):,.0f}")
        
        # Chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=forecast_df['date'], y=forecast_df['predicted'],
                                 mode='lines+markers', name='Forecast'))
        fig.add_trace(go.Scatter(x=forecast_df['date'], y=forecast_df['upper'],
                                 mode='lines', name='Upper', line=dict(dash='dash')))
        fig.add_trace(go.Scatter(x=forecast_df['date'], y=forecast_df['lower'],
                                 mode='lines', name='Lower', line=dict(dash='dash')))
        fig.update_layout(title='30-Day Sales Forecast', height=500)
        st.plotly_chart(fig, use_container_width=True)
        
        # Table
        with st.expander("View Forecast Data"):
            display_df = forecast_df.copy()
            display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
            display_df.columns = ['Date', 'Predicted', 'Lower', 'Upper']
            st.dataframe(display_df.round(2))
    else:
        st.error("❌ Failed to fetch forecast from backend")
        st.info(f"Backend URL: {BACKEND_URL}")
        st.code("Check if backend is running: curl http://127.0.0.1:8000/health")
else:
    st.error("⚠️ Backend not available")
    st.code("""
    # Start the backend:
    cd backend
    uvicorn api:app --reload --port 8000
    """)

# ==================== FOOTER ====================
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("Sales Intelligence Platform v2.0")
with col2:
    st.caption("Random Forest • 87.3% Accuracy")
with col3:
    status = "✅ Online" if BACKEND_AVAILABLE else "❌ Offline"
    st.caption(f"API: {status}")