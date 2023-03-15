import streamlit as st

import pandas as pd

import cohere_sdk

# Initialize the Cohere client SDK

cohere = cohere_sdk.Client(api_key='YOUR_API_KEY')

# Define a function to get embeddings for a list of text

def get_embeddings(texts):

    embeddings = cohere.embed(texts, model='your_model_name')

    return embeddings['outputs']

# Define a function to run k-means clustering on a set of embeddings

def run_clustering(embeddings, num_clusters):

    clustering = cohere.clustering(embeddings, num_clusters)

    return clustering['assignments']

# Define a function to concatenate text with the same cluster label

def concatenate_text(labels, text):

    clusters = {}

    for label, sentence in zip(labels, text):

        if label not in clusters:

            clusters[label] = []

        clusters[label].append(sentence)

    concatenated_text = {}

    for label in clusters:

        concatenated_text[label] = ' '.join(clusters[label])

    return concatenated_text

# Define a function to summarize a text using the Cohere summarizer

def summarize_text(text):

    summary = cohere.summarize(text, model='your_model_name')

    return summary['output']

# Define a function to generate a download link for a DataFrame

def download_link(df, file_name):

    csv = df.to_csv(index=False)

    b64 = base64.b64encode(csv.encode()).decode()

    href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}">Download {file_name}</a>'

    return href

# Define the main Streamlit app function

def main():

    st.title('Clustering and Summarization App')

    

    # Step 1: User uploads CSV file

    st.header('Step 1: Upload a CSV file')

    uploaded_file = st.file_uploader('Choose a file', type='csv')

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        

        # Step 2: Display contents of CSV file

        st.header('Step 2: Display contents of CSV file')

        st.write(df)

        

        # Step 3: Cluster and concatenate text

        st.header('Step 3: Cluster and concatenate text')

        with st.spinner('Clustering text...'):

            embeddings = get_embeddings(df['answer'].tolist())

            labels = run_clustering(embeddings, num_clusters=5)

            concatenated_text = concatenate_text(labels, df['answer'].tolist())

        

        # Step 4: Summarize text

        st.header('Step 4: Summarize text')

        with st.spinner('Summarizing text...'):

            summarized_text = {}

            for label in concatenated_text:

                summarized_text[label] = summarize_text(concatenated_text[label])

        

        # Step 5: Generate download link

        st.header('Step 5: Generate download link')

        result_df = pd.DataFrame({'cluster-label': list(summarized_text.keys()), 'summarized-text': list(summarized_text.values())})

        st.write(result_df)

        st.markdown(download_link(result_df, 'result.csv'), unsafe_allow_html=True)

if __name__ == '__main__':

    main()
