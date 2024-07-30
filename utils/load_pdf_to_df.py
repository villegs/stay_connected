import os
import config
from langchain.document_loaders import DirectoryLoader
import pandas as pd
from datetime import datetime
os.environ["GOOGLE_API_KEY"] = config.gemini_api_key

if __name__ == '__main__':
    directory_path = "../documents/output"
    loader = DirectoryLoader(directory_path, glob="*.pdf")
    documents = loader.load()
    list_dicts = []
    for doc in documents:

        name = doc.metadata['source'].split('\\')[-1]
        center = f'{name[-5]}'
        week = int(name[0] if not name[1].isnumeric() else name[0:2])
        content = doc.page_content.replace('#','').replace('*','').strip()
        dict_info = {
            'Center': center,
            'Week':week,
            'Content': content
        }
        list_dicts.append(dict_info)
    df = pd.DataFrame(list_dicts).set_index('Center')
    df['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df.to_csv('../center_reports.csv')
    df2 = pd.read_csv('../center_reports.csv', parse_dates=['Timestamp'])
