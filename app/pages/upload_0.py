import pandas as pd
import streamlit as st

# Step 1: User uploads CSV file
def uploadCSV(goto_next):
    st.header('Step 1: Upload a CSV file')
    uploaded_file = st.file_uploader('Choose a file', type='csv')

    if uploaded_file is not None:
        if 'file_name' not in st.session_state:
            st.session_state.file_name = uploaded_file.name
        df = pd.read_csv(uploaded_file)
        df = df.reset_index(drop=True)
        
        def nextStep():
            if 'df' not in st.session_state:
                st.session_state['df'] = df.head(200)
            goto_next()

        with st.form("uploader"):
            st.write(df.shape)
            st.table(df.head())
            st.form_submit_button(label='Next', on_click=nextStep)

        
        
        
            