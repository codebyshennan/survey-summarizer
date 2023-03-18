import streamlit as st

from app.helpers.cohere import CohereSDK


def generateEmbeds(goto_next):
    co = CohereSDK()
    selected_column = st.session_state.selected_column
    df = st.session_state.df
    
    st.header('Step 4: Generate Embeddings')
    
    data = {}
  
    with st.spinner('Generate embeddings...'):
      embdgs = co.get_cohere_embeddings(df, selected_column)
      
      for index, row in df.iterrows():
          text = row[selected_column]
          translated = row['translated_sentence']
          data[index] = {
              "text": text,
              "translated": translated,
              "embeddings": embdgs[index]
          }
    
    st.header("Select number of clusters")
      
    n_clusters = st.slider('Number of clusters', 1, 10, 5)
  
    with st.form("embeddings"):
      def nextStep():
        st.session_state.n_clusters = n_clusters
        st.session_state.data = data
        goto_next()
        
      st.form_submit_button(label='Submit', on_click=nextStep)
      