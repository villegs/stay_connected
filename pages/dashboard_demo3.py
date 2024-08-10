import streamlit as st
import pandas as pd
import altair as alt
from utils.load_and_join_df import retrieve_formatted_df
df = retrieve_formatted_df()

# Streamlit App
st.title("Hospital Performance Dashboard")

# Row 1: Center-Specific Metrics
col1, col2 = st.columns(2)

with col1:
    st.header("Center Performance")
    st.metric("Number of Patients", df["Number of Patients"][0], delta=None)
    st.metric("Average Time to Get Served", df["Average Time to Get Served"][0], delta=None, help="Minutes")
    st.metric(
        "Patient Satisfaction Score",
        df["Patient Satisfaction Scores"][0],
        delta=None,
        help="Out of 5",
    )

with col2:
    st.header("Staff Performance")
    st.metric(
        "Number of Staff Training Hours",
        df["Number of Staff Training Hours"][0],
        delta=None,
    )
    st.metric(
        "Turnover Rate of Staff",
        df["Turnover Rate of Staff"][0],
        delta=None,
        help="Percentage",
    )

# Row 2: Time-Series Charts
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Time-Series Metrics")
    st.write(
        "This chart needs historical data for multiple weeks. Please provide sample data for a few weeks to see the chart."
    )
    chart = alt.Chart(df).mark_line().encode(
        x="Week:Q",
        y="Number of Patients:Q",
    )
    st.altair_chart(chart)

with col2:
    st.header("Resource Utilization")
    st.metric(
        "Bed Occupancy Rate",
        df["Bed Occupancy Rate"][0],
        delta=None,
        help="Percentage",
    )
    st.metric(
        "Utilization of Equipment & Resources",
        df["Utilization of Equiment & Resources"][0],
        delta=None,
        help="Percentage",
    )

# Row 3: Line Chart Column for Average Time to Get Served
st.header("Average Time to Get Served by Urgency")
serve_time_cols = [
                    "Average Time to Get Served (Urgent)",
                    "Average Time to Get Served (Semi-Urgent)",
                    "Average Time to Get Served (Non-Urgent)",
                ]
df_urgency = df[['Center', 'Week',*serve_time_cols]].copy()
df_urgency = pd.melt(df_urgency,id_vars=[col for col in df_urgency.columns if col not in serve_time_cols],value_vars=serve_time_cols,var_name='Urgency', value_name='Average Time to Get Served')
df_urgency['Urgency'] = df_urgency['Urgency'].str.split(' ').str.get(-1).str[1:-1]
# st.dataframe(df_urgency)
# Create a dropdown for selecting the center
center_selection = st.selectbox("Select Center", df_urgency['Center'].unique())

# Filter data based on the selected center
filtered_data = df_urgency[df_urgency['Center'] == center_selection]

# Create Altair chart
chart = alt.Chart(filtered_data).mark_line().encode(
    x='Week:N',
    y='Average Time to Get Served:Q',
    color='Urgency:N',
    tooltip=['Week', 'Urgency', 'Average Time to Get Served']
).properties(
    title=f"Average Time to Get Served - {center_selection}"
)

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)
# chart = (
#     alt.Chart(df_urgency)
#     # alt.Chart(df)
#     .mark_line()
#     .encode(
#         alt.X("Week:Q", title="Week"),
#         alt.Y(
#             "Average Time to Get Served:Q",
#             title="Average Time (Minutes)",
#             scale=alt.Scale(domain=[0, 60]),
#         ),
#         alt.Color(
#             "Urgency",
#             scale=alt.Scale(
#                 domain=serve_time_cols,
#                 range=["red", "orange", "green"],
#             ),
#         ),
#     )
# )
# st.altair_chart(chart)

# Row 4: Table with Key Metrics
st.header("Key Metrics")
st.dataframe(
    df[
        [
            "Number of Patients",
            "Average Time to Get Served",
            "Patient Satisfaction Scores",
            "Bed Occupancy Rate",
            "Turnover Rate of Staff",
            "Average Cost per Patient",
        ]
    ].style.format("{:.2f}")
)

# Row 5: Location Details
st.header("Location Details")
st.write(f"**Region:** {df['Region'][0]}")
st.write(f"**Commune:** {df['Commune'][0]}")
st.write(f"**City:** {df['City'][0]}")
st.write(f"**Population:** {df['Population'][0]}")

# Row 6: Additional Data
st.header("Additional Data")
st.write("**Number of Readmissions:**", df["Number of Readmissions"][0])
st.write(
    "**Number of Medical Licenses Presented:**",
    df["Number of Medical Licenses Presented"][0],
)
st.write(
    "**Number of  Supplies Ordered/Consumed:**",
    df["Number of  Supplies Ordered/Consumed"][0],
)
st.write(
    "**Number of Outpatient Appointments:**",
    df["Number of Outpatient Appointments"][0],
)
st.write(
    "**Number of Emergency Room Visits:**",
    df["Number of Emergency Room Visits"][0],
)
st.write(
    "**Number of Surgical Procedures Performed:**",
    df["Number of Surgical Procedures Performed"][0],
)