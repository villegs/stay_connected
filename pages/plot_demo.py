import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataframe (replace with your actual data)
data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
        'Value': [10, 20, 15, 25, 18, 12, 30]}
df = pd.DataFrame(data)

# Streamlit app
st.title('Data Visualization')

# Select aggregation method
aggregation_method = st.selectbox('Select Aggregation Method', ['Sum', 'Mean', 'Count'])

# Select column to group by
group_by_column = st.selectbox('Select Group By Column', df.columns)

# Perform aggregation
if aggregation_method == 'Sum':
    aggregated_data = df.groupby(group_by_column)['Value'].sum()
elif aggregation_method == 'Mean':
    aggregated_data = df.groupby(group_by_column)['Value'].mean()
elif aggregation_method == 'Count':
    aggregated_data = df.groupby(group_by_column)['Value'].count()

# Create bar chart
fig, ax = plt.subplots()
aggregated_data.plot(kind='bar', ax=ax)
ax.set_xlabel(group_by_column)
ax.set_ylabel('Aggregated Value')
ax.set_title(f'{aggregation_method} of Value by {group_by_column}')

# Display chart in Streamlit
st.pyplot(fig)