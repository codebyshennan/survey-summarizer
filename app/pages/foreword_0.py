import streamlit as st


def foreword(goto_next):
  
  st.write("What this app is about:")
  st.write("In many instances where you have to analyse survey results, that are conducted in various languages (esp in Southeast Asia where more than 2000 languages are practiced), you will need to translate the survey results into English before you can analyse them. Thereafter, you will need to cluster the translated results into groups to understand the ground sentiment. This app will help you do that.")
  
  st.header("Resource required")
  metric_col1, metric_col2, metric_col3 = st.columns(3)
  metric_col1.metric("Manpower", "Just 1", "90%")
  metric_col2.metric("Cost", "$0", "100%")
  metric_col3.metric("Time", "3 mins", "90%")
  
  explain_col1, explain_col2, explain_col3 = st.columns(3)
  explain_col1.write("Do not require a team of data scientists, data engineers, and data analysts to work on this project.")
  explain_col2.write("Do not require any money to be spent on this project. Just upload your CSV and it's done.")
  explain_col3.write("What might take a team of data scientists 1 months to complete, can be done in 3 minutes with this app.")
  
  with st.form("uploader"):
    st.form_submit_button(label='Next', on_click=goto_next)
