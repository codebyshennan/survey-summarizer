import time

import streamlit as st
from helpers.cohere import co


def summariseLabelGroups(goto_next):
  n_clusters = st.session_state.n_clusters
  df_labelled = st.session_state.df_labelled
  
  label_text_dict = {}
  
  st.header("Step 6: Summarise label groups")
  st.write("For each label group, we then run a summariser using Cohere's API to summarise the sentences in that group. This gives us a clearer idea of what each group is about. As we are using a free API, we have to wait 15 seconds between each request, and we can only make 5 API calls per minute.")
  
  progress_text = "Operation in progress. Please wait."
  bar = st.progress(0, text=progress_text)
  

  with st.spinner():
    for label in range(n_clusters):
      rows = df_labelled[df_labelled['cluster'] == label]
      
      translated_text = ' '.join(rows['translated'].tolist())
      label_text_dict[label] = translated_text
    
    el = st.text(len(label_text_dict))
  
  # length of label_text_dict
  dict_length = len(label_text_dict.keys())
  
  summaries = []

  
  for i, k in enumerate(label_text_dict):
    
    label = k
    text_string = label_text_dict[k]
    
    response = co.summarize_text(
      text_string
    )
    
    summaries.append([label, response.summary])
    
    bar.progress((i+1) * (100 // dict_length), text=progress_text)
    el.text(f"{len(summaries)}/{dict_length} completed")
    time.sleep(15)
    
  st.table(summaries)
  
  with st.form("summarise"):
    def nextStep():
      if 'summaries' not in st.session_state:
        st.session_state.summaries = summaries
      goto_next()
      
    st.form_submit_button('Next', on_click=nextStep)