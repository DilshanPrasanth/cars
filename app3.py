import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Set the path to the CSV file
csv_file_path = Path(r'C:\Users\Saman\Desktop\phyton_ws\AUS.Vechile Prices\Australian Vehicle Prices.csv')

# Load the data
df = pd.read_csv(csv_file_path)

# Streamlit application
st.title("Australian Vehicle Prices Dashboard")

# Display the DataFrame
st.write("## Car Dataset")
st.dataframe(df)

# Display basic statistics
st.write("## Basic Statistics")
st.write(df.describe())

# Data visualization - Scatter plot
st.write("## Kilometres vs Price")
scatter_fig = px.scatter(df, x='Kilometres', y='Price', color='Year', title='Kilometres vs Price')
st.plotly_chart(scatter_fig)

# Data visualization - Bar chart
st.write("## Average Price by Brand")
bar_fig = px.bar(df, x='Brand', y='Price', color='Brand', title='Average Price by Brand')
st.plotly_chart(bar_fig)

# Data visualization - Box plot
st.write("## Price Distribution by Fuel Type")
box_fig = px.box(df, x='FuelType', y='Price', color='FuelType', title='Price Distribution by Fuel Type')
st.plotly_chart(box_fig)

# Data visualization - Histogram
st.write("## Price Distribution")
hist_fig = px.histogram(df, x='Price', nbins=50, title='Price Distribution')
st.plotly_chart(hist_fig)

# Data visualization - Pie chart
st.write("## Fuel Type Distribution")
pie_fig = px.pie(df, names='FuelType', title='Fuel Type Distribution')
st.plotly_chart(pie_fig)
