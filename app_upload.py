import streamlit as st
# import requests
import google.generativeai as genai

import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import PyPDF2

def display_pdf(pdf_file):
    """
    Displays a PDF file in Streamlit.

    Args:
        pdf_file (str): Path to the PDF file.
    """

    with open(pdf_file, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        # Display a dropdown to select the page
        page_num = st.selectbox("Select page", range(1, num_pages + 1), index=0)

        # Extract and display the selected page
        page = pdf_reader.pages[page_num - 1]
        st.markdown('Previewing PDF')
        st.markdown(page.extract_text())

def markdown_to_pdf(markdown_text, filename=None):
  """Saves markdown text to a PDF file."""

  # Create a PDF document
  if filename is None:
      filename = "output.pdf"
  doc = SimpleDocTemplate(filename, pagesize=letter)

  # Create a list to store the content
  story = []

  # Get the default stylesheet
  styles = getSampleStyleSheet()

  # Convert markdown to ReportLab elements
  for line in markdown_text.splitlines():
    if line.startswith("#"):
      # Heading
      heading_level = len(line) - 1
      story.append(Paragraph(line[heading_level:], styles["Heading%s" % heading_level]))
    else:
      # Normal text
      story.append(Paragraph(line, styles["Normal"]))
      story.append(Spacer(1, 0.2 * inch))

  # Build the document
  doc.build(story)


# the_prompt = """
# Consider first what elements can be used in public services for keeping track of productivity and resource allocation, for example average time to get served, separated by level of importance, number of medical licenses presented this week, etc.
# List these elements, and use this list, to generate a dummy weekly report as if you were a director of one of the medical branches of the hospital, lets say, surgeon, pediatrics or any other.
# Do not include any name in the report.
# """

st.title("SC Management")

# Get API key from user secrets
gemini_api_key = st.secrets["gemini_api_key"]
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
            # st.json(response)
            st.markdown(response.text)
            pdf_file = "output.pdf"
            markdown_to_pdf(response.text, filename=pdf_file)
            display_pdf(pdf_file)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide both API key and query.")