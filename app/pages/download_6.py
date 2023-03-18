import streamlit as st
import pandas as pd

@st.cache_data
def convert_df(list, headers):
    df = pd.DataFrame(list, columns=headers)
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def downloadResult(goto_next):
  headers = ['label', 'summary']  
  summaries = st.session_state.summaries
  file_name = st.session_state.file_name
  
  csv = convert_df(summaries, headers)
  
  st.download_button(
      label="Download data as CSV",
      data=csv,
      file_name=f'{file_name}_labels_and_summary.csv',
      mime='text/csv',
  )
