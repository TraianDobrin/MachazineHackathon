# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import csv

app = Flask(__name__)
CORS(app)

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load data and precompute embeddings
data = []
with open('../embeddings.csv', newline='', encoding='utf-8', errors='ignore') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        cleaned_row = [cell.encode('utf-8', 'ignore').decode('utf-8', 'ignore') for cell in row]
        if row[0] == "path":
            continue
        cleaned_row[1] = cleaned_row[1].strip('[]')
        if len(cleaned_row) == 2:
            data.append((cleaned_row[0], np.array([float(num) for num in cleaned_row[1].split()]).reshape(1, -1)))

def search_specifications(query, data, model):
    query_embedding = model.encode([query])[0].reshape(1, -1)
    similarities = []
    for (path, description) in data:
        similarity = cosine_similarity(query_embedding, description)[0][0]
        similarities.append((similarity, path))
    similarities.sort(key=lambda x: x[0], reverse=True)
    return similarities

@app.route('/search', methods=['POST'])
def search():
    content = request.json
    specifications = content['specifications']
    nr_results = int(content['nr_results'])
    matching_docs = search_specifications(specifications, data, model)
    results = [{"path": doc[1]} for doc in matching_docs[:nr_results]]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
