from sentence_transformers import SentenceTransformer, util
from bs4 import BeautifulSoup

def clean_text(text: str):
  return BeautifulSoup(text, "html.parser").get_text()


def compare_text(text_A: str, text_B: str):
  model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
  sentences = [clean_text(text_A), clean_text(text_B)]
  embeddings = model.encode(sentences)
  similarity = util.cos_sim(embeddings[0], embeddings[1])
  return round(similarity.item(), 2)