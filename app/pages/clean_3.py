import streamlit as st
from helpers.csv import clean_df


def cleanText(goto_next):
  st.header('Step 3: Clean text')
  st.write("Before we proceed with the clustering, we need to clean the text. This step removes all words that are shorter than the minimum length you specify. This step is optional, but it is recommended to remove words that are too short to be meaningful.")
  
  df = st.session_state.df
  selected_column = st.session_state.selected_column


  # create a streamlit table with the dataframe
  
  # clean datasource
  min_length = st.slider('Minimum length of words', 1, 10, 0)

  st.write('Min Length:', min_length)
  st.write('Selected Column:', selected_column)
  
  if min_length >= 1:
    with st.spinner('Cleaning text...'):
      cleaned_df = clean_df(df, selected_column, min_length)
      st.table(cleaned_df.head())
      st.write(cleaned_df.shape)
      
    with st.form("clean_text"):
      def nextStep():
        st.session_state.cleaned_df = cleaned_df
        goto_next()
        
      st.form_submit_button(label='Selected', on_click=nextStep)