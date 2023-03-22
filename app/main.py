
import sys

import streamlit as st
from pages.clean_3 import cleanText
from pages.cluster_5 import gatherClusters
from pages.conclusion_7 import conclusion
from pages.download_8 import downloadResult
from pages.embed_4 import generateEmbeds
from pages.filter_2 import filterDf
from pages.foreword_0 import foreword
from pages.summarise_6 import summariseLabelGroups
from pages.upload_1 import uploadCSV

print(sys.path)

def go_to_next_page():
    st.session_state.page_no += 1


def main():
    
    if 'page_no' not in st.session_state:
        st.session_state['page_no'] = 0
        
    pages = {
        0: foreword,
        1: uploadCSV,
        2: filterDf,
        3: cleanText,
        4: generateEmbeds,
        5: gatherClusters,
        6: summariseLabelGroups,
        7: conclusion,
        8: downloadResult,
    }

    st.title('Multilingual Text Summarisation')
    
    pages[st.session_state.page_no](go_to_next_page)

if __name__ == '__main__':
    main()
