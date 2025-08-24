import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 GitHub Practice Dashboard")

# Sidebar
st.sidebar.header("Settings")
option = st.sidebar.selectbox("Choose chart type:", ["Line", "Bar"])

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("./data/data.csv")

df = load_data()

# Show dataframe
st.subheader("Dataset Preview")
st.write(df.head())

# Plot chart
st.subheader("Visualization")
fig, ax = plt.subplots()

if option == "Line":
    ax.plot(df["Month"], df["Value"], marker="o")
    ax.set_title("Line Chart")
else:
    ax.bar(df["Month"], df["Value"])
    ax.set_title("Bar Chart")

st.pyplot(fig)
