import streamlit as st

# Set page title
st.set_page_config(page_title="Streamlit Container App", layout="wide")

# Main title
st.title("Streamlit Container App")

# Function to load CSV files
# @st.cache_data
# def load_csv(file_path):
#     return pd.read_csv(file_path)

# List of CSV files
# csv_files = [
# ]

# Add a footer
st.markdown("---")
st.markdown("Created by @tooniez")
