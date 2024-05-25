from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
import numpy as np

# Initialize the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")
index_name = "product_specifications"

# Define the index configuration
index_config = {
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "embedding": {"type": "dense_vector", "dims": 384},
            "path": {"type": "keyword"}
        }
    }
}

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=index_config)

# Index the data
for text, path in data:
    embedding = model.encode(text).tolist()
    doc = {
        "text": text,
        "embedding": embedding,
        "path": path
    }
    es.index(index=index_name, body=doc)