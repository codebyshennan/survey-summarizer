import os

from cohere import Client


class CohereSDK():
  def __init__(self) -> None:
    self.api_key = os.environ.get("COHERE_API_KEY")
    self.client = Client(self.api_key)
  
  def get_cohere_embeddings(self, df, selected):

    text_array = [row[selected] for _, row in df.iterrows()]

    # get the embeddings
    return self.client.embed(texts=text_array, model='multilingual-22-12').embeddings

  # Define a function to get embeddings for a list of text

  def get_embeddings(self, texts, model_name):
    embeddings = self.client.embed(texts, model=model_name)
    return embeddings['outputs']

  # Define a function to run k-means clustering on a set of embeddings
  def run_clustering(self, embeddings, num_clusters):
    clustering = self.client.clustering(embeddings, num_clusters)
    return clustering['assignments']
  
  def summarize_text(self, text, length):
    return self.client.summarize(
      text=text, 
      length=length, 
      format='paragraph',
      model='summarize-xlarge',
      extractiveness='low',
      temperature=0.3
    )

