import streamlit as st
# import requests
import google.generativeai as genai

st.title("Gemini API Client")

# Get API key from user secrets
gemini_api_key = st.secrets["gemini_api_key"]
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def send_request_to_gemini(query):

    return response.json()


st.title("Gemini API Request")

# Input fields for API key and query
# api_key = st.text_input("API Key", type="password")
query = st.text_area("Query")

# Send request button
if st.button("Send Request"):
    if gemini_api_key and query:
        try:
            response = model.generate_content(query)
            st.success("Request sent successfully!")
            # st.json(response)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide both API key and query.")