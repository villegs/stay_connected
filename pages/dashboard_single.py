import streamlit as st
import pandas as pd
import altair as alt
from utils.load_and_join_df import retrieve_formatted_df
df_all = retrieve_formatted_df()
center_selection = st.selectbox("Select Center", df_all['Center'].unique())
df = df_all[df_all['Center']==center_selection].reset_index()
# Streamlit App
st.title("Hospital Performance Dashboard")



# Filter data based on the selected center
serve_time_cols = [
                    "Average Time to Get Served (Urgent)",
                    "Average Time to Get Served (Semi-Urgent)",
                    "Average Time to Get Served (Non-Urgent)",
                ]
df_urgency = df[['Center', 'Week',*serve_time_cols]].copy()
df_urgency = pd.melt(df_urgency,id_vars=[col for col in df_urgency.columns if col not in serve_time_cols],value_vars=serve_time_cols,var_name='Urgency', value_name='Average Time to Get Served')
df_urgency['Urgency'] = df_urgency['Urgency'].str.split(' ').str.get(-1).str[1:-1]


filtered_data = df_urgency[df_urgency['Center'] == center_selection]
# Row 1: Center-Specific Metrics
col1, col2 = st.columns(2)

with col1:
    st.header("Center Performance")
    st.metric(
        "Number of Patients",
        round(df["Number of Patients"].mean()),
        delta=None)
    st.metric(
        "Average Time to Get Served",
        round(df["Average Time to Get Served"].mean()),
        delta=None,
        help="Minutes"
    )
    st.metric(
        "Patient Satisfaction Score",
        round(df["Patient Satisfaction Scores"].mean()),
        delta=None,
        help="Out of 5",
    )

with col2:
    st.header("Staff Performance")
    st.metric(
        "Number of Staff Training Hours",
        round(df["Number of Staff Training Hours"].mean()),
        delta=None,
    )
    st.metric(
        "Turnover Rate of Staff",
        round(df["Turnover Rate of Staff"].mean()),
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
        round(df["Bed Occupancy Rate"].mean()),
        delta=None,
        help="Percentage",
    )
    st.metric(
        "Utilization of Equipment & Resources",
        round(df["Utilization of Equiment & Resources"].mean()),
        delta=None,
        help="Percentage",
    )

# Row 3: Line Chart Column for Average Time to Get Served
st.header("Average Time to Get Served by Urgency")

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
st.write("**Number of Readmissions:**", round(df["Number of Readmissions"].mean()))
st.write(
    "**Number of Medical Licenses Presented:**",
    round(df["Number of Medical Licenses Presented"].mean()),
)
st.write(
    "**Number of  Supplies Ordered/Consumed:**",
    round(df["Number of  Supplies Ordered/Consumed"].mean()),
)
st.write(
    "**Number of Outpatient Appointments:**",
    round(df["Number of Outpatient Appointments"].mean()),
)
st.write(
    "**Number of Emergency Room Visits:**",
    round(df["Number of Emergency Room Visits"].mean()),
)
st.write(
    "**Number of Surgical Procedures Performed:**",
    round(df["Number of Surgical Procedures Performed"].mean()),
)