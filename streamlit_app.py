import streamlit as st

# This file allows Streamlit Cloud to auto-detect the app
# Import and run the main app
if __name__ == "__main__":
    import sys
    # Import app.py which is the Streamlit frontend
    exec(open("app.py").read())
