import streamlit as st
from helpers.cohere import co


def generateEmbeds(goto_next):
    selected_column = st.session_state.selected_column
    cleaned_df = st.session_state.cleaned_df
    
    st.header('Step 4: Generate Embeddings')
    st.write("Select number of clusters")
      
    n_clusters = st.slider('Number of clusters', 1, 10, 5)
    
    data = {}

    if n_clusters > 1:
      with st.spinner('Generate embeddings...'):
        embdgs = co.get_cohere_embeddings(cleaned_df, selected_column)
        
        for index, row in cleaned_df.iterrows():
            text = row[selected_column]
            translated = row['translated_sentence']
            data[index] = {
                "text": text,
                "translated": translated,
                "embeddings": embdgs[index]
            }
  
    with st.form("embeddings"):
      def nextStep():
        st.session_state.n_clusters = n_clusters
        st.session_state.data = data
        goto_next()
        
      st.form_submit_button(label='Selected', on_click=nextStep)
      