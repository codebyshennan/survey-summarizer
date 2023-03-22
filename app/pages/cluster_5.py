import numpy as np
import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans


def gatherClusters(goto_next):
    n_clusters = st.session_state.n_clusters
    data = st.session_state.data

    st.header('Step 5: Gather Clusters')
    st.header(f"Number of clusters: {n_clusters}")
    st.write("The following table shows the number of sentences in each cluster.")
    
    with st.spinner('Gathering clusters...'):
        texts = []
        translated = []
        embeddings = []
        
        for k, v in data.items():
            texts.append(v['text'])
            translated.append(v['translated'])
            embeddings.append(v['embeddings'])
        
        X = np.array(embeddings)
        kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
        labels = kmeans.labels_
        
        df_labelled = pd.DataFrame({'text': texts, 'translated': translated, 'cluster': labels})
        
    with st.form("embeddings"):
        # group by cluster and write to streamlit table
        st.table(df_labelled.groupby('cluster').agg({'text': 'count'}))
        
        def nextStep():
            st.session_state.df_labelled = df_labelled
            st.session_state.n_clusters = n_clusters
            st.session_state.data = data
            goto_next()

        st.form_submit_button(label='Submit', on_click=nextStep)
