import streamlit as st
import tabs.home as home
import tabs.JK as JK
import tabs.JJ as JJ
import tabs.VZV as VZV
import tabs.ER as ER

# Set page title and layout
st.set_page_config(page_title="Buying vs Renting", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "JK", "JJ", "VZV", "ER"])

# Home Screen
if options == "Home":
    home.show_home()

# Tab 1
elif options == "JK":
    JK.show_home()

# Tab 2
elif options == "JJ":
    JJ.show_home()

# Tab 3
elif options == "VZV":
    VZV.show_home()

# Tab 4
elif options == "ER":
    ER.show_home()
