import streamlit as st
from PIL import Image

logo_image = Image.open('logo.jpeg')

st.set_page_config(
    page_title="Stay Connected",
    page_icon="🏥",
    layout="wide"
)
# Set the layout
# st.set_page_config(layout="wide")

# Create a container for the logo
logo_container = st.container()

# Add the logo to the container
with logo_container:
  col1, col2 = st.columns([1, 10])
  with col1:
    st.image(logo_image, width=100)
# logo_image = Image.open("logo.jpeg")  # Replace with the path to your logo image
#
# # Display the logo in the sidebar
# st.sidebar.image(logo_image, width=150)
    with col2:
        # Title and subtitle
        st.title("Stay Connected: Your Healthcare Data Hub")
        st.subheader("Effortlessly gather, analyze, and visualize your healthcare data.")

        # Introduction
        st.markdown(
            """
            Stay Connected is your one-stop solution for managing and analyzing healthcare data from your centers. 
            We make it easy to:
        
            * **Collect weekly reports** from multiple healthcare centers in a standardized format.
            * **Automate data extraction** using Gemini's powerful language processing capabilities.
            * **Transform raw data into insightful tables** ready for analysis.
            * **Generate interactive visualizations** to identify trends and patterns.
            """
        )
        # Key Features
        st.header("Key Features")
        st.markdown(
            """
            - **Streamlined data collection:**  Submit reports easily through a user-friendly interface.
            - **Automated data extraction:**  Gemini parses reports for key data points with high accuracy.
            - **Comprehensive analysis:**  Generate charts, tables, and dashboards to understand your data.
            - **Real-time insights:**  Track progress and identify areas for improvement instantly.
            """
        )
        # Image of the app in action
        st.header("Stay connected in action")
        image = Image.open("app_screenshot.png")  # Replace with your actual image
        st.image(image, caption="Stay Connected in action", width=700)



        # Call to action
        st.markdown(
            """
            Ready to take control of your healthcare data? 
            **Get started with Stay Connected today!**
            """
        )
