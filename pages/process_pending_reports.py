from utils.reports import *
import streamlit as st

df_reports = pd.read_csv('center_reports.csv', parse_dates=['Timestamp'], dayfirst=True).set_index(['Center','Week'])
df_reports_table = pd.read_csv('reports_table.csv', parse_dates=['Timestamp'], dayfirst=True).set_index(['Center','Week'])
df_report_definition = pd.read_csv('report_table_definition.csv')
df_filtered = df_reports[~df_reports.index.isin(df_reports_table.index)]
st.subheader('Pending reports to be converted:')
# Display filtered DataFrame
st.dataframe(df_filtered)

# Radio button to select the DataFrame
df_choice = st.radio("Select what reports to process:", ('pending', 'all'))

# Button to trigger the processing
if st.button("Process"):
    if df_choice == 'pending':
        with st.spinner('Processing pending entries'):
            processed_df = transform_reports_to_table(df_filtered.reset_index(),df_report_definition)
            st.write("Processed pending reports:")
            st.dataframe(processed_df)
            processed_df = pd.concat([df_reports_table, processed_df])
            processed_df.to_csv('reports_table.csv')
    elif df_choice == 'all':
        with st.spinner('Processing all entries'):
            processed_df = transform_reports_to_table(df_reports,df_report_definition)
            st.write("Processed all reports:")
            st.dataframe(processed_df)
            processed_df.to_csv('reports_table.csv')
