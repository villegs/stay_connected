import pandas as pd

def load_centers(tab='report_request'):
    """Returns dictionary with keys being the center and inside them its the metrics dictionary."""
    df = pd.read_excel(r'D:\Projects\stay_connected\documents\setup\metrics_and_data.xlsx',tab)
    df = df.rename(columns={'Unnamed: 0':'Metric'})
    df = df.set_index('Metric')
    dict_centers = df.to_dict()
    return dict_centers