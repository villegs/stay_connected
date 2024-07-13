import streamlit as st
# import requests
import google.generativeai as genai
import os
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import PyPDF2
from df_load import load_centers
import time
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
      heading_level = min(heading_level,6)
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

base_query = """
Do a report with the following considerations:
-It must be at most one page long and as if written in a formal report.
-Title must be center name plus week information plus "report".
-Information of the report must be taken from the "Metrics" field.
-During winter, the metrics should have a random increase, without exceeding 100% for occupancy.
-Center A to C are hospitals.
-Center D to Z are health clinics.
-Replace the week number with the corresponding real dates.
-Weeks starts on Mondays, so the first week of 2023 would be from monday 2 to sunday 8.
-Can use the example at the bottom as reference.
-The report should have a title.
-Use a high temperature of about 0.6 for the report.
-Week to be used is: {} of 2023
-Center: {}
-Metrics: {}

Example - Start:

Center A - Week 1 of 2023 Report

This report details the key performance indicators for Center A during the first week of 2023, covering the period from January 2nd to January 8th.

Patient Volume and Care:

Center A served a total of 6,000 patients during this period. The average time for patients to be served was 30 minutes. Analyzing the data based on urgency levels, patients categorized as "Urgent" waited an average of 10 minutes, "Semi-Urgent" patients waited 20 minutes, and "Non-Urgent" patients waited an average of 45 minutes. Patient satisfaction scores averaged 4.2, indicating a positive overall experience.

Operational Efficiency:

The number of readmissions for the week was 50, suggesting potential areas for improvement in post-discharge care. 100 medical licenses were presented, ensuring proper staff credentialing. A total of 500 staff training hours were dedicated to enhancing skills and knowledge. The utilization rate of equipment and resources was 85%, indicating efficient resource allocation. Center A ordered and consumed 10,000 supplies, highlighting the high volume of patient care provided. The turnover rate of staff stood at 10%, which is within the acceptable range.

Financial Performance and Outpatient Services:

The average cost per patient was $500. Center A saw 2,000 outpatient appointments, showcasing a strong commitment to community health. There were 500 emergency room visits, indicating a high demand for acute care services. 300 surgical procedures were performed, reflecting the center's capability in surgical interventions. The bed occupancy rate was 70%, demonstrating high utilization of available resources.
Example - End
"""
output_path = r'documents\output'
# Input fields for API key and query
# api_key = st.text_input("API Key", type="password")
dict_center_keys = load_centers().keys()
dict_weeks = {i: load_centers(f'Week {i}') for i in range(1,54)}
for center in dict_center_keys:
    for week in range(1,54):
        query = base_query.format(str(week), center,str(dict_weeks[week][center]))
        response = model.generate_content(query)
        st.success("Request sent successfully!")
        st.markdown(response.text)
        pdf_file = os.path.join(output_path, f"{week}{center}.pdf")
        markdown_to_pdf("   "+response.text, filename=pdf_file)
        time.sleep(20)

