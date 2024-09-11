import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Buying vs Renting", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Jacobus K", "Jacobus J", "Van Zyl", "Eddie"])

# Home Screen
if options == "Home":
    st.title("Welcome to the Buying vs Renting App")
    st.write("This is the home page. Use the sidebar to navigate through the tabs.")

# Tab 1
elif options == "Jacobus K":
    st.title("Tab 1")
    st.write("This is Tab 1 content.")
    # You can add more components here

# Tab 2
elif options == "Jacobus J":
    st.title("Tab 2")
    st.write("This is Tab 2 content.")
    # You can add more components here

# Tab 3
elif options == "Van Zyl":
    st.title("Tab 2")
    st.write("This is Tab 2 content.")
    # You can add more components here

# Tab 4
elif options == "Eddie":
    st.title("Tab 2")
    st.write("This is Tab 2 content.")
    # You can add more components here
