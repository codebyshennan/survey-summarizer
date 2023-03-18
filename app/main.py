
import streamlit as st
import sys


from app.pages.clean_2 import cleanText
from app.pages.cluster_4 import gatherClusters
from app.pages.download_6 import downloadResult
from app.pages.embed_3 import generateEmbeds
from app.pages.filter_1 import filterDf
from app.pages.summarise_5 import summariseLabelGroups
from app.pages.upload_0 import uploadCSV


print(sys.path)

def go_to_next_page():
    st.session_state.page_no += 1


def main():
    

    
    if 'page_no' not in st.session_state:
        st.session_state['page_no'] = 0
        
    pages = {
        0: uploadCSV,
        1: filterDf,
        2: cleanText,
        3: generateEmbeds,
        4: gatherClusters,
        5: summariseLabelGroups,
        6: downloadResult,
    }

    st.title('Clustering and Summarization App')
    st.write('This app clusters and summarizes text from a CSV file.')
    
    pages[st.session_state.page_no](go_to_next_page)

if __name__ == '__main__':
    main()
