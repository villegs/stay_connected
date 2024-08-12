import streamlit as st
import pandas as pd
import numpy as np
from utils.load_and_join_df import retrieve_formatted_df
df = retrieve_formatted_df()

# Set up Streamlit page title
st.title("All metrics linechart")

# Define the columns for your line chart
line_chart_columns = [
    "Number of Patients",
    "Average Time to Get Served",
    "Average Time to Get Served (Urgent)",
    "Average Time to Get Served (Semi-Urgent)",
    "Average Time to Get Served (Non-Urgent)",
    "Patient Satisfaction Scores",
    "Number of Readmissions",
    "Number of Medical Licenses Presented",
    "Number of Staff Training Hours",
    "Utilization of Equiment & Resources",
    "Number of  Supplies Ordered/Consumed",
    "Turnover Rate of Staff",
    "Average Cost per Patient",
    "Number of Outpatient Appointments",
    "Number of Emergency Room Visits",
    "Number of Surgical Procedures Performed",
    "Bed Occupancy Rate",
]

# Create the column configurations for the dataframe
column_configs = {
    "Center": "Center",
    # "Week": "Week",
}
for column in line_chart_columns:
    column_configs[column] = st.column_config.LineChartColumn(
        column, y_min=0, y_max=df[column].max() * 1.2
    )  # Adjust y_max as needed

# This should be configurable
st.dataframe(
    df.interpolate(method='linear', limit_direction='forward', axis=0).fillna(np.nan).groupby('Center')[line_chart_columns].agg(list).reset_index(),
    height=None,
    use_container_width=True,
    column_config=column_configs,
    hide_index=True,
)