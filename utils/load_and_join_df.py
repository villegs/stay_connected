import pandas as pd
from datetime import datetime
import os
import streamlit as st

def retrive_latest(df, timestamp, columns):
    """It will return the latest entry based on 'Timestamp' column <= timestamp.
     It will be grouped by 'columns' to get the latest Timestamp available."""
    df = df[df['Timestamp'] <= timestamp]
    filtered = df.groupby(columns)['Timestamp'].max().reset_index()
    final_df = filtered.merge(df,'left',[*columns,'Timestamp'])
    final_df = final_df.drop(columns=['Timestamp'])
    return final_df

@st.cache_data
def retrieve_formatted_df(timestamp=None, file_path=None):
    if timestamp is None:
        timestamp = datetime.now()
    if file_path is None:
        file_path = ''
    df_reports = pd.read_csv(os.path.join(file_path,'reports_table.csv'), parse_dates=['Timestamp'], dayfirst=True)
    df_reports = retrive_latest(df_reports, timestamp, ['Center','Week'])
    df_center_info = pd.read_csv(os.path.join(file_path,'center_info.csv'), parse_dates=['Timestamp'], dayfirst=True)
    df_center_info = retrive_latest(df_center_info, timestamp, ['Center'])
    df_city_info = pd.read_csv(os.path.join(file_path,'city_info.csv'), parse_dates=['Timestamp'], dayfirst=True)
    df_city_info = retrive_latest(df_city_info, timestamp, ['City'])
    df = df_reports.merge(df_center_info,'left','Center').merge(df_city_info, 'left', 'City')
    df = df.sort_values(['Center','Week'])
    return df

if __name__ == '__main__':
    df = retrieve_formatted_df(file_path='..')
