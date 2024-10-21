import streamlit as st
from pages import home, data_generation, eda, playground, download

# Set page title
st.set_page_config(page_title="Streamlit Multi-Page App", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Generation", "EDA", "Playground", "Download"])

# Main title
st.title("Streamlit Multi-Page App")

# Display the selected page
if page == "Home":
    home.show()
elif page == "Data Generation":
    data_generation.show()
elif page == "EDA":
    eda.show()
elif page == "Playground":
    playground.show()
elif page == "Download":
    download.show()

# Add a footer
st.markdown("---")
st.markdown("Created by @tooniez")
