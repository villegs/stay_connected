import google.generativeai as genai
import streamlit as st

import config

st.title("Stay Connected")

# Get API key from user secrets
gemini_api_key = config.gemini_api_key
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Input fields for API key and query
# api_key = st.text_input("API Key", type="password")
query = st.text_area("Query")

# Send request button
if st.button("Send Request"):
    if gemini_api_key and query:
        try:
            response = model.generate_content(query)
            st.success("Request sent successfully!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide both API key and query.")