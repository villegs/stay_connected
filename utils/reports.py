import google.generativeai as genai
import os
import config
import pandas as pd
import json

genai.configure(api_key=config.gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


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

def parse_report_definition(df_report_definition):
    str_output = f"Column, Type, Example \n"
    for index, row in df_report_definition.iterrows():
        str_output += f"{row['Column']}, {row['Type']}, {row['Example']} \n"
    return str_output


def transform_reports_to_table(df_reports, df_report_definition, request_size=100):
    list_df = []
    for i in range((df_reports.shape[0] // request_size) + 1):
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
            Table definition:```{parse_report_definition(df_report_definition)}```
            Reports: {parse_reports(df_reports[i * request_size:(i + 1) * request_size])}

        """
        response = model.generate_content(query)
        dict_response = json.loads(response.text.replace('json', '').replace('```', ''))
        df_response = pd.DataFrame(dict_response)
        list_df.append(df_response)
    df_output = pd.concat(list_df)
    df_output = df_output.set_index(['Center','Week'])
    # df_output.to_csv('../reports_table.csv')
    return df_output
