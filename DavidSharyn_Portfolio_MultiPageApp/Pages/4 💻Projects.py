import streamlit as st

st.title("📂 Featured Projects")

with st.expander("🌾 Weather-Monitoring & Decision Support System"):
    st.write("""
    A real-time dashboard powered by Google Weather API for the DEBESMSCAT farm.
    - **Stakeholders:** Agriculture Dean Mr. Michael O. Ogaya
    - **Key Feature:** Early-warning notifications for crop management.
    """)
    st.info("Status: Active Thesis Project")

with st.expander("🛒 Shopping Cart Simulation"):
    st.write("A modular system built using Python's functional decomposition principles.")