import streamlit as st
from utils.transform_report_to_table import parse_reports
import pandas as pd
import google.generativeai as genai
import config

genai.configure(api_key=config.gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Set up Streamlit page title
st.title("Ask the reports")

def ask_about_reports(question, df):
    query = f"""
        Based on reports below, answer the following: {question}
        ```
        Reports: {parse_reports(df)}
    
    """
    response = model.generate_content(query)
    return response

df = pd.read_csv('center_reports.csv', parse_dates=['Timestamp'])
question = """
Make a summary of key finding, always including metrics in a table to backup the explanation, the response
 should consider the following points:
-Find trends that would lead to complications from the centers
-Find if any Center will need help
-Rank best Centers
"""
query = st.text_area("Query")

# Send request button
if st.button("Send Request"):
    try:
        response = ask_about_reports(query, df)
        st.markdown(response.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")
