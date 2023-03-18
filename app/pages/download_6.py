import streamlit as st


@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def downloadResult():
  summaries = st.session_state.summaries
  file_name = st.session_state.file_name
  
  csv = convert_df(summaries)
  
  st.download_button(
      label="Download data as CSV",
      data=csv,
      file_name=f'{file_name}_labels_and_summary.csv',
      mime='text/csv',
  )
