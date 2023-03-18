import streamlit as st
from app.helpers.translate import translate_sentence

def filterDf(goto_next):
  
  st.header('Step 2: Cluster and concatenate text')
  
  df = st.session_state.df
  col = ['-'] + [col for col in df if not col.startswith('Unnamed')]
  # select column to filter by
  selected_column = st.selectbox('Select column to filter by', col)
  
  if selected_column != '-':
    progress_text = "Operation in progress. Please wait."
    bar = st.progress(0, text=progress_text)
    el = st.text("0 completed")
    total = len(df.index)
    
    translations = []
    
    for sentence in df[selected_column]:
        translation = translate_sentence(sentence)

        translations.append(translation)
        bar.progress(len(translations) * (100//total))
        el.text(f"{len(translations) * (100//total)} completed")
      
    df['translated_sentence'] = translations
    
    with st.form("cluster"):
      # create a streamlit table with the dataframe
      st.table(df.head())
      st.write(df.shape)

      def next_page():
        st.session_state.df = df
        if 'selected_column' not in st.session_state:
          st.session_state['selected_column'] = selected_column
        goto_next()

      st.form_submit_button(label='Submit', on_click=next_page)
          