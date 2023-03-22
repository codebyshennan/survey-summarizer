import streamlit as st
from helpers.cohere import co


def conclusion(goto_next):
  
  st.header('Step 7: Conclusive Summary')
  st.write("We can also generate a summary of the text that we have clustered. This is useful for summarising the results of the clustering.")
  with st.spinner('Summarising...'):
    summaries = st.session_state.summaries
    combined = ' '.join([f"{s[0]}: {s[1]}" for s in summaries])
    
    response = co.summarize_text(combined)
    
    st.write(response.summary)
    
    with st.form("summarise"):
      def nextStep():
        if 'full_summary' not in st.session_state:
          st.session_state.full_summary = response.summary
        goto_next()
        
      st.form_submit_button('Next', on_click=nextStep)