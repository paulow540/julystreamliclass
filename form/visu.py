import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Set page config
st.set_page_config(page_title="Data Visualization Dashboard", layout="wide")

# Title
st.title("📊 Data Visualization Dashboard")
st.markdown("---")

# Sample data generation
@st.cache_data
def generate_sample_data():
    np.random.seed(42)
    categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Sports']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    
    data = {
        'Category': categories * 6,
        'Month': sorted(months * 5),
        'Sales': np.random.randint(100, 1000, 30),
        'Profit': np.random.randint(20, 200, 30)
    }
    df = pd.DataFrame(data)
    return df

df = generate_sample_data()

# Sidebar for controls
st.sidebar.header("📈 Chart Controls")

# Chart type selection
chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    ["Bar Chart", "Pie Chart", "Line Chart", "All Charts"]
)

# Data filtering
selected_categories = st.sidebar.multiselect(
    "Select Categories",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

selected_months = st.sidebar.multiselect(
    "Select Months",
    options=df['Month'].unique(),
    default=df['Month'].unique()
)

# Filter data based on selections
filtered_df = df[
    (df['Category'].isin(selected_categories)) & 
    (df['Month'].isin(selected_months))
]

# Main content
if chart_type in ["Bar Chart", "All Charts"]:
    st.header("📊 Bar Chart")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Sales by Category
        fig_bar_sales = px.bar(
            filtered_df.groupby('Category')['Sales'].sum().reset_index(),
            x='Category',
            y='Sales',
            title='Total Sales by Category',
            color='Category'
        )
        st.plotly_chart(fig_bar_sales, use_container_width=True)
    
    with col2:
        # Sales by Month
        fig_bar_month = px.bar(
            filtered_df.groupby('Month')['Sales'].sum().reset_index(),
            x='Month',
            y='Sales',
            title='Total Sales by Month',
            color='Month'
        )
        st.plotly_chart(fig_bar_month, use_container_width=True)

if chart_type in ["Pie Chart", "All Charts"]:
    st.header("🥧 Pie Chart")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Sales distribution by category
        category_sales = filtered_df.groupby('Category')['Sales'].sum()
        fig_pie_sales = px.pie(
            values=category_sales.values,
            names=category_sales.index,
            title='Sales Distribution by Category'
        )
        st.plotly_chart(fig_pie_sales, use_container_width=True)
    
    with col2:
        # Profit distribution by category
        category_profit = filtered_df.groupby('Category')['Profit'].sum()
        fig_pie_profit = px.pie(
            values=category_profit.values,
            names=category_profit.index,
            title='Profit Distribution by Category'
        )
        st.plotly_chart(fig_pie_profit, use_container_width=True)

if chart_type in ["Line Chart", "All Charts"]:
    st.header("📈 Line Chart")
    
    # Time series line chart
    time_series_data = filtered_df.groupby(['Month', 'Category'])['Sales'].sum().reset_index()
    
    fig_line = px.line(
        time_series_data,
        x='Month',
        y='Sales',
        color='Category',
        title='Sales Trend by Category Over Time',
        markers=True
    )
    st.plotly_chart(fig_line, use_container_width=True)
    
    # Multiple metrics line chart
    st.subheader("Multiple Metrics Comparison")
    
    metrics_data = filtered_df.groupby('Month')[['Sales', 'Profit']].sum().reset_index()
    
    fig_line_multi = px.line(
        metrics_data,
        x='Month',
        y=['Sales', 'Profit'],
        title='Sales vs Profit Trend',
        markers=True
    )
    st.plotly_chart(fig_line_multi, use_container_width=True)

# Data summary
st.markdown("---")
st.header("📋 Data Summary")

col1, col2, col3 = st.columns(3)

with col1:
    total_sales = filtered_df['Sales'].sum()
    st.metric("Total Sales", f"${total_sales:,}")

with col2:
    total_profit = filtered_df['Profit'].sum()
    st.metric("Total Profit", f"${total_profit:,}")

with col3:
    avg_sale = filtered_df['Sales'].mean()
    st.metric("Average Sale", f"${avg_sale:,.2f}")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.dataframe(filtered_df)

# Download button
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)