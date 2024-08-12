import streamlit as st
from utils.reports import parse_reports
import pandas as pd
import google.generativeai as genai
import config

genai.configure(api_key=config.gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-pro')

# Set up Streamlit page title
st.title("Ask the reports")

# Introduction
st.markdown(
    """
    Select what reports should be taken into consideration, then provide a prompt to ask about the
     information in the reports.
    ## Example:
    Make a summary of key findings, always including metrics in a table to backup the explanation, 
        the response should consider the following points:
    * **Find trends that would lead to complications from the centers.**
    * **Find if any Center will need help.**
    * **Rank best Centers.**
    """
)

df = pd.read_csv('center_reports.csv', parse_dates=['Timestamp'])

# Sidebar for filtering
st.sidebar.header("Filters")
selected_center = st.sidebar.multiselect("Select Center", df['Center'].unique())
selected_week = st.sidebar.multiselect("Select Week", df['Week'].unique())

# Apply filters
filtered_df = df
if selected_center:
    filtered_df = filtered_df[filtered_df['Center'].isin(selected_center)]
if selected_week:
    filtered_df = filtered_df[filtered_df['Week'].isin(selected_week)]
filtered_df=filtered_df

st.subheader('Report information:')
# Display filtered DataFrame
st.dataframe(filtered_df.set_index('Center'))

def ask_about_reports(question, df):
    query = f"""
        Based on reports below, answer the following: {question}
        Reports: {parse_reports(df)}
    """
    response = model.generate_content(query)
    return response

query = st.text_area("Query")

# Send request button
if st.button("Send Request"):
    try:
        with st.spinner(text="In progress..."):
            response = ask_about_reports(query, filtered_df)
            st.markdown(response.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")
