import streamlit as st
import pandas as pd
import altair as alt

# Sample Data - Replace with your actual dataframe
df = pd.read_csv('reports_table.csv', parse_dates=['Timestamp'])
df = df.sort_values(['Center','Week'])

# Streamlit App
st.title("Healthcare Center Performance Dashboard")

# Sidebar for Filters
st.sidebar.header("Filters")
center_filter = st.sidebar.multiselect(
    "Select Center(s)", df['Center'].unique(), default=df['Center'].unique()
)
week_filter = st.sidebar.slider(
    "Select Week Range",
    int(df['Week'].min()),
    int(df['Week'].max()),
    (int(df['Week'].min()), int(df['Week'].max())),
)

# Apply Filters
filtered_df = df[
    (df['Center'].isin(center_filter)) & (df['Week'] >= week_filter[0]) & (df['Week'] <= week_filter[1])
]

# KPIs
kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Patients", filtered_df["Number of Patients"].sum())
kpi2.metric("Average Time to Get Served", filtered_df["Average Time to Get Served"].mean())
kpi3.metric("Patient Satisfaction Score", filtered_df["Patient Satisfaction Scores"].mean())

# Chart 1: Time to Get Served by Urgency
st.subheader("Average Time to Get Served by Urgency Level")
chart_data = filtered_df[['Week', 'Average Time to Get Served (Urgent)',
                         'Average Time to Get Served (Semi-Urgent)',
                         'Average Time to Get Served (Non-Urgent)']]
chart_data = chart_data.melt(
    id_vars='Week', value_vars=['Average Time to Get Served (Urgent)',
                                'Average Time to Get Served (Semi-Urgent)',
                                'Average Time to Get Served (Non-Urgent)'],
    var_name='Urgency Level', value_name='Average Time (Minutes)'
)
alt_chart = alt.Chart(chart_data).mark_line().encode(
    x='Week',
    y='Average Time (Minutes)',
    color='Urgency Level'
)
st.altair_chart(alt_chart, use_container_width=True)

# Chart 2: Bed Occupancy Rate Over Time
st.subheader("Bed Occupancy Rate Over Time")
alt_chart = alt.Chart(filtered_df).mark_line().encode(
    x='Week',
    y='Bed Occupancy Rate'
)
st.altair_chart(alt_chart, use_container_width=True)

# Table with Detailed Data
st.subheader("Detailed Data")
st.dataframe(filtered_df)