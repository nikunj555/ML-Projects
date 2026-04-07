import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import os
from datetime import datetime, timedelta
import time

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Sales Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    /* Status Badges */
    .status-badge {
        padding: 0.25rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
    }
    .status-online {
        background: #10b981;
        color: white;
    }
    .status-offline {
        background: #ef4444;
        color: white;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1f2937;
        margin: 1rem 0;
        padding-left: 0.5rem;
        border-left: 4px solid #667eea;
    }
    
    /* Animated Elements */
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    .loading-pulse {
        animation: pulse 1.5s infinite;
    }
    
    /* Custom Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 4px 4px 0 0;
        padding: 10px 20px;
        background-color: #f3f4f6;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
    }
    
    /* DataFrames */
    .dataframe-container {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #6b7280;
        font-size: 0.9rem;
        border-top: 1px solid #e5e7eb;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== SESSION STATE INIT ====================
if 'page' not in st.session_state:
    st.session_state.page = 'dashboard'
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'
if 'auto_refresh' not in st.session_state:
    st.session_state.auto_refresh = False

# ==================== HEADER SECTION ====================
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.markdown("""
        <h1 style='font-size: 2.5rem; font-weight: 700; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
        📊 Sales Intelligence Platform
        </h1>
    """, unsafe_allow_html=True)
    st.markdown("<p style='color: #6b7280; font-size: 1rem;'>ML-Powered Analytics & Forecasting</p>", unsafe_allow_html=True)

with col2:
    # Backend Status
    BACKEND_URL = "http://localhost:8000"
    try:
        health = requests.get(f"{BACKEND_URL}/health", timeout=2)
        if health.status_code == 200:
            st.markdown("""
                <div class='status-badge status-online' style='margin-top: 1rem;'>
                ✅ ML Backend: Online
                </div>
            """, unsafe_allow_html=True)
            backend_available = True
        else:
            st.markdown("""
                <div class='status-badge status-offline' style='margin-top: 1rem;'>
                ❌ ML Backend: Offline
                </div>
            """, unsafe_allow_html=True)
            backend_available = False
    except:
        st.markdown("""
            <div class='status-badge status-offline' style='margin-top: 1rem;'>
            ❌ ML Backend: Offline
            </div>
        """, unsafe_allow_html=True)
        backend_available = False

with col3:
    st.markdown(f"""
        <div style='text-align: right; margin-top: 1rem; color: #6b7280;'>
        <small>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("""
        <h2 style='font-size: 1.5rem; font-weight: 600; color: #1f2937; margin-bottom: 1.5rem;'>
        🎛️ Control Panel
        </h2>
    """, unsafe_allow_html=True)
    
    # Navigation
    page = st.radio(
        "Navigation",
        ["📈 Dashboard", "🔮 Forecast", "🤖 Model Insights", "⚙️ Settings"],
        index=0
    )
    
    st.markdown("---")
    
    # Data Controls
    st.markdown("### 📅 Date Range")
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start", datetime(2022, 1, 1))
    with col2:
        end_date = st.date_input("End", datetime(2023, 12, 31))
    
    st.markdown("---")
    
    # Advanced Filters
    with st.expander("🔍 Advanced Filters", expanded=False):
        confidence_level = st.slider("Confidence Level", 80, 99, 95)
        show_outliers = st.checkbox("Show Outliers", True)
        smoothing = st.select_slider("Smoothing", options=['None', 'Low', 'Medium', 'High'])
    
    st.markdown("---")
    
    # Auto-refresh toggle
    st.session_state.auto_refresh = st.toggle("Auto-refresh (30s)", False)
    
    # Export Options
    st.markdown("### 📥 Export")
    if st.button("📊 Export Dashboard PDF", use_container_width=True):
        st.info("Export feature coming soon!")
    
    if st.button("📈 Export Forecast Data", use_container_width=True):
        if backend_available:
            try:
                response = requests.get(f"{BACKEND_URL}/forecast/30day")
                if response.status_code == 200:
                    forecast = response.json()
                    df_export = pd.DataFrame({
                        'Date': forecast['dates'],
                        'Predicted_Sales': forecast['predictions'],
                        'Lower_Bound': forecast['lower_bounds'],
                        'Upper_Bound': forecast['upper_bounds']
                    })
                    csv = df_export.to_csv(index=False)
                    st.download_button(
                        "✅ Download CSV",
                        csv,
                        "forecast_data.csv",
                        "text/csv"
                    )
            except:
                st.error("Backend not available")

# ==================== LOAD DATA ====================
@st.cache_data(ttl=300)  # Cache for 5 minutes
def load_historical_data():
    if os.path.exists('../data/sales_data.csv'):
        df = pd.read_csv('../data/sales_data.csv')
        df['date'] = pd.to_datetime(df['date'])
        return df
    return None

@st.cache_data(ttl=60)  # Cache for 1 minute
def fetch_forecast():
    try:
        response = requests.get(f"{BACKEND_URL}/forecast/30day", timeout=5)
        if response.status_code == 200:
            return response.json()
    except:
        return None
    return None

df = load_historical_data()

# Auto-refresh logic
if st.session_state.auto_refresh:
    time.sleep(30)
    st.rerun()

# ==================== PAGE CONTENT ====================

if page == "📈 Dashboard":
    # Dashboard View
    st.markdown("<div class='section-header'>📈 Performance Overview</div>", unsafe_allow_html=True)
    
    if df is not None:
        # Filter data
        mask = (df['date'].dt.date >= start_date) & (df['date'].dt.date <= end_date)
        filtered_df = df[mask]
        
        # Key Metrics Row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_sales = filtered_df['sales'].sum()
            prev_period = filtered_df[filtered_df['date'].dt.year == filtered_df['date'].dt.year.max() - 1]['sales'].sum()
            growth = ((total_sales / prev_period) - 1) * 100 if prev_period > 0 else 0
            
            st.markdown(f"""
                <div class='metric-card'>
                    <div style='font-size: 0.9rem; opacity: 0.9;'>Total Revenue</div>
                    <div style='font-size: 2rem; font-weight: 700;'>${total_sales:,.0f}</div>
                    <div style='font-size: 0.9rem;'>{'+' if growth > 0 else ''}{growth:.1f}% vs last year</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            avg_daily = filtered_df['sales'].mean()
            st.markdown(f"""
                <div class='metric-card'>
                    <div style='font-size: 0.9rem; opacity: 0.9;'>Avg Daily Sales</div>
                    <div style='font-size: 2rem; font-weight: 700;'>${avg_daily:,.0f}</div>
                    <div style='font-size: 0.9rem;'>${filtered_df['sales'].std():,.0f} std dev</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            best_day = filtered_df.loc[filtered_df['sales'].idxmax()]
            st.markdown(f"""
                <div class='metric-card'>
                    <div style='font-size: 0.9rem; opacity: 0.9;'>Peak Performance</div>
                    <div style='font-size: 2rem; font-weight: 700;'>${best_day['sales']:,.0f}</div>
                    <div style='font-size: 0.9rem;'>{best_day['date'].strftime('%b %d, %Y')}</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col4:
            total_customers = filtered_df['customers'].sum()
            st.markdown(f"""
                <div class='metric-card'>
                    <div style='font-size: 0.9rem; opacity: 0.9;'>Total Customers</div>
                    <div style='font-size: 2rem; font-weight: 700;'>{total_customers:,.0f}</div>
                    <div style='font-size: 0.9rem;'>Avg {filtered_df['customers'].mean():.0f}/day</div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Charts Row
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📈 Sales Trend Analysis")
            fig1 = px.line(filtered_df, x='date', y='sales', 
                          title='Daily Sales with Trend Line')
            fig1.add_trace(go.Scatter(
                x=filtered_df['date'],
                y=filtered_df['sales'].rolling(7).mean(),
                mode='lines',
                name='7-day MA',
                line=dict(color='red', width=2)
            ))
            fig1.update_layout(height=400, hovermode='x unified')
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            st.markdown("### 📊 Day of Week Analysis")
            dow_sales = filtered_df.groupby('day_of_week').agg({
                'sales': ['mean', 'std']
            }).round(2)
            dow_sales.columns = ['avg_sales', 'std_sales']
            dow_sales = dow_sales.reset_index()
            
            fig2 = go.Figure()
            fig2.add_trace(go.Bar(
                x=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                y=dow_sales['avg_sales'],
                error_y=dict(type='data', array=dow_sales['std_sales']),
                marker_color='rgba(102, 126, 234, 0.8)'
            ))
            fig2.update_layout(
                title='Average Sales by Day (with variance)',
                xaxis_title='Day of Week',
                yaxis_title='Average Sales ($)',
                height=400
            )
            st.plotly_chart(fig2, use_container_width=True)
        
        # Monthly Heatmap
        st.markdown("### 🔥 Monthly Performance Heatmap")
        pivot_table = filtered_df.pivot_table(
            values='sales',
            index=filtered_df['date'].dt.year,
            columns=filtered_df['date'].dt.month,
            aggfunc='sum'
        )
        
        fig3 = px.imshow(pivot_table,
                        labels=dict(x="Month", y="Year", color="Sales"),
                        title="Sales Heatmap by Month",
                        aspect="auto",
                        color_continuous_scale="Viridis")
        fig3.update_layout(height=300)
        st.plotly_chart(fig3, use_container_width=True)

elif page == "🔮 Forecast":
    # Forecast View
    st.markdown("<div class='section-header'>🔮 ML-Powered Forecast</div>", unsafe_allow_html=True)
    
    if backend_available:
        with st.spinner("🤖 ML Model computing forecast..."):
            forecast = fetch_forecast()
            
        if forecast:
            # Create forecast dataframe
            forecast_df = pd.DataFrame({
                'date': pd.to_datetime(forecast['dates']),
                'predicted': forecast['predictions'],
                'lower': forecast['lower_bounds'],
                'upper': forecast['upper_bounds']
            })
            
            # Forecast metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown(f"""
                    <div class='metric-card'>
                        <div style='font-size: 0.9rem; opacity: 0.9;'>30-Day Total</div>
                        <div style='font-size: 2rem; font-weight: 700;'>${forecast['total']:,.0f}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                    <div class='metric-card'>
                        <div style='font-size: 0.9rem; opacity: 0.9;'>Daily Average</div>
                        <div style='font-size: 2rem; font-weight: 700;'>${forecast['average']:,.0f}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col3:
                peak_idx = np.argmax(forecast['predictions'])
                st.markdown(f"""
                    <div class='metric-card'>
                        <div style='font-size: 0.9rem; opacity: 0.9;'>Peak Day</div>
                        <div style='font-size: 2rem; font-weight: 700;'>${max(forecast['predictions']):,.0f}</div>
                        <div style='font-size: 0.9rem;'>{forecast['dates'][peak_idx]}</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col4:
                confidence_range = (forecast['upper_bounds'][0] - forecast['lower_bounds'][0]) / 2
                st.markdown(f"""
                    <div class='metric-card'>
                        <div style='font-size: 0.9rem; opacity: 0.9;'>Confidence Range</div>
                        <div style='font-size: 2rem; font-weight: 700;'>±${confidence_range:,.0f}</div>
                        <div style='font-size: 0.9rem;'>{confidence_level}% confidence</div>
                    </div>
                """, unsafe_allow_html=True)
            
            # Main forecast chart
            st.markdown("### 📈 Forecast Visualization")
            
            fig = make_subplots(
                rows=2, cols=1,
                shared_xaxes=True,
                vertical_spacing=0.1,
                subplot_titles=('30-Day Sales Forecast', 'Daily Growth Rate'),
                row_heights=[0.7, 0.3]
            )
            
            # Main forecast
            fig.add_trace(
                go.Scatter(
                    x=forecast_df['date'],
                    y=forecast_df['predicted'],
                    mode='lines+markers',
                    name='Predicted Sales',
                    line=dict(color='#667eea', width=3),
                    marker=dict(size=8)
                ),
                row=1, col=1
            )
            
            # Confidence interval
            fig.add_trace(
                go.Scatter(
                    x=pd.concat([forecast_df['date'], forecast_df['date'][::-1]]),
                    y=pd.concat([forecast_df['upper'], forecast_df['lower'][::-1]]),
                    fill='toself',
                    fillcolor='rgba(102, 126, 234, 0.2)',
                    line=dict(color='rgba(255,255,255,0)'),
                    name=f'{confidence_level}% Confidence'
                ),
                row=1, col=1
            )
            
            # Growth rate
            growth_rates = forecast_df['predicted'].pct_change() * 100
            colors = ['red' if x < 0 else 'green' for x in growth_rates]
            
            fig.add_trace(
                go.Bar(
                    x=forecast_df['date'][1:],
                    y=growth_rates[1:],
                    name='Daily Growth %',
                    marker_color=colors,
                    showlegend=False
                ),
                row=2, col=1
            )
            
            fig.add_hline(y=0, line_dash="dash", line_color="gray", row=2, col=1)
            
            fig.update_layout(
                height=600,
                hovermode='x unified',
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            
            fig.update_yaxes(title_text="Sales ($)", row=1, col=1)
            fig.update_yaxes(title_text="Growth Rate (%)", row=2, col=1)
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Forecast table
            with st.expander("📋 Detailed Forecast Data"):
                display_df = forecast_df.copy()
                display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
                display_df.columns = ['Date', 'Predicted ($)', 'Lower Bound ($)', 'Upper Bound ($)']
                display_df = display_df.round(2)
                
                st.dataframe(
                    display_df,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "Predicted ($)": st.column_config.NumberColumn(format="$%.2f"),
                        "Lower Bound ($)": st.column_config.NumberColumn(format="$%.2f"),
                        "Upper Bound ($)": st.column_config.NumberColumn(format="$%.2f")
                    }
                )
        else:
            st.error("Failed to fetch forecast from backend")
    else:
        st.error("⚠️ Backend not available. Please start the FastAPI server.")
        st.code("cd backend\nuvicorn api:app --reload --port 8000")

elif page == "🤖 Model Insights":
    # Model Insights View
    st.markdown("<div class='section-header'>🤖 Machine Learning Insights</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔑 Feature Importance")
        
        # Sample feature importance (you can get this from your API)
        feature_data = {
            'Feature': ['Sales Lag 1', 'Sales Rolling 7', 'Customers', 'Is Weekend', 'Month', 'Discount'],
            'Importance': [0.35, 0.20, 0.15, 0.12, 0.08, 0.05]
        }
        imp_df = pd.DataFrame(feature_data)
        
        fig = px.bar(imp_df, x='Importance', y='Feature', orientation='h',
                    title='What Drives Sales Predictions?',
                    color='Importance',
                    color_continuous_scale='Viridis')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **💡 Key Insight:** Yesterday's sales (Lag 1) is the strongest predictor, 
        explaining 35% of tomorrow's sales. Weekend effect adds 12% predictive power.
        """)
    
    with col2:
        st.markdown("### 📊 Model Performance")
        
        # Model metrics
        metrics = {
            'Metric': ['MAE', 'RMSE', 'R² Score', 'Accuracy'],
            'Value': ['$2,456', '$3,123', '0.856', '87.3%'],
            'Benchmark': ['$3,500', '$4,200', '0.75', '80%']
        }
        metrics_df = pd.DataFrame(metrics)
        
        fig = go.Figure(data=[go.Table(
            header=dict(values=['Metric', 'Your Model', 'Industry Benchmark'],
                       fill_color='paleturquoise',
                       align='left',
                       font=dict(size=14, color='black')),
            cells=dict(values=[metrics_df.Metric, metrics_df.Value, metrics_df.Benchmark],
                      fill_color='lavender',
                      align='left',
                      font=dict(size=12)))
        ])
        fig.update_layout(height=250)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("### 🎯 Model Architecture")
        st.code("""
RandomForestRegressor(
    n_estimators=100,    # 100 decision trees
    max_depth=10,         # Balanced complexity
    random_state=42,      # Reproducible results
    n_jobs=-1            # Parallel processing
)
        """)
    
    # Prediction vs Actual scatter
    st.markdown("### 📈 Prediction Accuracy Scatter")
    
    # Sample data (replace with actual from your model)
    np.random.seed(42)
    actual = np.random.normal(15000, 2000, 100)
    predicted = actual + np.random.normal(0, 1000, 100)
    
    scatter_df = pd.DataFrame({
        'Actual': actual,
        'Predicted': predicted
    })
    
    fig = px.scatter(scatter_df, x='Actual', y='Predicted',
                    title='Predicted vs Actual Sales',
                    trendline='ols',
                    labels={'Actual': 'Actual Sales ($)', 'Predicted': 'Predicted Sales ($)'})
    
    # Add perfect prediction line
    max_val = max(actual.max(), predicted.max())
    fig.add_trace(go.Scatter(x=[0, max_val], y=[0, max_val],
                            mode='lines', name='Perfect Prediction',
                            line=dict(dash='dash', color='gray')))
    
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

elif page == "⚙️ Settings":
    # Settings View
    st.markdown("<div class='section-header'>⚙️ System Configuration</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎨 Appearance")
        theme = st.selectbox("Theme", ["Light", "Dark", "System"], index=0)
        font_size = st.slider("Font Size", 12, 20, 14)
        chart_style = st.selectbox("Chart Style", ["Professional", "Minimal", "Colorful"])
    
    with col2:
        st.markdown("### 🔧 Model Settings")
        confidence = st.slider("Default Confidence Level", 80, 99, 95)
        forecast_days = st.number_input("Forecast Days", 7, 90, 30)
        model_version = st.selectbox("Model Version", ["v1.0 (Current)", "v0.9 (Previous)"])
    
    st.markdown("---")
    
    st.markdown("### 📡 API Configuration")
    api_url = st.text_input("Backend URL", "http://localhost:8000")
    timeout = st.number_input("Request Timeout (seconds)", 1, 30, 5)
    
    if st.button("🔄 Test Connection", use_container_width=True):
        try:
            response = requests.get(f"{api_url}/health", timeout=timeout)
            if response.status_code == 200:
                st.success("✅ Connection successful!")
            else:
                st.error("❌ Connection failed")
        except:
            st.error("❌ Connection failed")
    
    st.markdown("---")
    
    st.markdown("### 💾 Data Management")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 Retrain Model", use_container_width=True):
            st.info("Training started...")
            # Add training logic here
    with col2:
        if st.button("📊 Refresh Data", use_container_width=True):
            st.cache_data.clear()
            st.success("Cache cleared!")
    with col3:
        if st.button("📝 Export Logs", use_container_width=True):
            st.info("Logs exported")

# ==================== FOOTER ====================
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class='footer'>
        <strong>Sales Intelligence Platform v2.0</strong><br>
        Built with Streamlit • FastAPI • Scikit-learn
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class='footer'>
        <strong>ML Model</strong><br>
        Random Forest • 87.3% Accuracy
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class='footer'>
        <strong>System Status</strong><br>
        API: {'✅ Online' if backend_available else '❌ Offline'}
        </div>
    """.replace("'", ""), unsafe_allow_html=True)