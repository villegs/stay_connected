import streamlit as st
import pandas as pd
import plotly.express as px

from utils.load_and_join_df import retrieve_formatted_df
df = retrieve_formatted_df()

# Streamlit App
st.title('Dynamic Data Aggregation and Plotting')

st.sidebar.header('User Input Features')
numerical_features = df.select_dtypes(include='number').columns.tolist()
numerical_features = [col for col in numerical_features if col not in  ['Week','Population']]
non_numerical_features = [col for col in df.columns if col not in numerical_features]
features = st.sidebar.multiselect('Select features to plot', options=numerical_features, default=numerical_features)

agg_option = st.sidebar.selectbox('Select aggregation function', options=['sum', 'mean', 'max', 'min'])

st.write("### Original Data")
st.write(df)

if len(features) > 0:
    # Allow grouping by all columns
    group_by_feature = st.sidebar.selectbox('Select feature to group by', options=non_numerical_features)

    if group_by_feature:
        agg_data = df.groupby(group_by_feature)[numerical_features].agg(agg_option).reset_index()

        st.write(f"### Aggregated Data ({agg_option.capitalize()}) by {group_by_feature}")
        st.write(agg_data)

        plot_option = st.sidebar.selectbox('Select plot type', options=['bar', 'line', 'scatter'])

        if plot_option == 'bar':
            fig = px.bar(agg_data, x=group_by_feature, y=[col for col in agg_data.columns if col != group_by_feature],
                         title=f"{agg_option.capitalize()} Aggregation of Features by {group_by_feature}")
        elif plot_option == 'line':
            fig = px.line(agg_data, x=group_by_feature, y=[col for col in agg_data.columns if col != group_by_feature],
                          title=f"{agg_option.capitalize()} Aggregation of Features by {group_by_feature}")
        elif plot_option == 'scatter':
            fig = px.scatter(agg_data, x=group_by_feature,
                             y=[col for col in agg_data.columns if col != group_by_feature],
                             title=f"{agg_option.capitalize()} Aggregation of Features by {group_by_feature}")

        st.plotly_chart(fig)

st.write("### Data Visualization")
st.write(f"Displaying {agg_option} aggregation of selected features grouped by {group_by_feature}")