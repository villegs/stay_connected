
import google.generativeai as genai
import os
import config
import pandas as pd
import json
genai.configure(api_key=config.gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

df = pd.read_csv('../center_reports.csv', parse_dates=['Timestamp'])

def parse_reports(df):
    str_output = "The following are entries of reports, enclosed by ```:"
    for index, row in df.iterrows():
        weekly_report_formatted = f"""
            ```
                Center: {row['Center']}
                Week: {row['Week']}
                Content: {row['Content']}
            ```
        """
        str_output += weekly_report_formatted
    return str_output
df_filtered = df

req_size = 100
list_df = []
for i in range((df_filtered.shape[0]//req_size)+1):
# for i in range(1):
    query = f"""
        Transform the weekly reports into a table.
        Considerations:
        -output must be passed in JSON format as to be able to create a pdf from it
        -the table information is detailed in the table definition
        -one row will correspond to one combination of center and week center and one week
        -table definition will be wrapped by ```
        -weekly reports will be wrapped by ```
        -do not include the word json or backticks in the response
        Table definition:```Column, Type, Example
        Center, str, Center A
        Week, int, 3
        Number of Patients, int, 6634
        Average Time to Get Served, int, 23
        Average Time to Get Served (Urgent), int, 22
        Average Time to Get Served (Semi-Urgent), int, 22
        Average Time to Get Served (Non-Urgent), int, 22
        Patient Satisfaction Scores, float,	3
        Number of Readmissions, int, 35
        Number of Medical Licenses Presented, int, 108
        Number of Staff Training Hours, float, 350
        Utilization of Equiment & Resources, float, 60
        Number of  Supplies Ordered/Consumed, integer, 7000
        Turnover Rate of Staff, int, 7
        Average Cost per Patient, int, 585
        Number of Outpatient Appointments, int, 2587
        Number of Emergency Room Visits, int, 350
        Number of Surgical Procedures Performed, int, 210
        Bed Occupancy Rate, float, 77
        Timestamp, str, 26-07-2024 20:25
        ```
        Reports: {parse_reports(df_filtered[i*req_size:(i+1)*req_size])}
    
    """
    response = model.generate_content(query)
    dict_response = json.loads(response.text.replace('json','').replace('```',''))
    df_response = pd.DataFrame(dict_response)
    list_df.append(df_response)
df_output = pd.concat(list_df)
df_output = df_output.set_index('Center')
df_output.to_csv('../reports_table.csv')