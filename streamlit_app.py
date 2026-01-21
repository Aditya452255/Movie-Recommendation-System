"""
Streamlit Cloud entry point.
Simply runs app.py which is the Streamlit frontend.
"""
import subprocess
import sys

# Run app.py as the Streamlit app
if __name__ == "__main__":
    exec(open("app.py").read())

