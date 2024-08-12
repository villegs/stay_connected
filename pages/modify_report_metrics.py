import streamlit as st
import pandas as pd

st.title("Edit report table definition")
df = pd.read_csv('report_table_definition.csv')
# Display dataframe
st.dataframe(df)


col1, col2 = st.columns(2)
with col1:
    # Add row button
    new_col = st.text_input("Column:")
    new_type = st.text_input("Type:")
    new_example = st.text_input("Example:")
    if st.button("Add Row"):
        new_row = pd.DataFrame({'Column': [new_col], 'Type': [new_type], 'Example':[new_example]})
        df = pd.concat([df, new_row], ignore_index=True)
        st.dataframe(df)

with col2:
    # Delete row button
    row_index = st.number_input("Enter row index to delete:", min_value=0, max_value=len(df)-1)
    if st.button("Delete Row"):
        df = df.drop(index=row_index)
        st.dataframe(df)


if st.button("Save changes"):
    df.to_csv('report_table_definition.csv')