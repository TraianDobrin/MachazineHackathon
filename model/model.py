from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import csv

# Initialize the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample data: list of tuples containing descriptions and file paths
data = []

with open('products.csv', newline='', encoding='utf-8', errors='ignore') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    # Iterate over each row in the CSV file
    for row in reader:
        # Remove any characters that cannot be decoded
        cleaned_row = [cell.encode('utf-8', 'ignore').decode('utf-8', 'ignore') for cell in row]
        # Assuming each row has two columns, create a tuple with the values and append it to the list
        if len(cleaned_row) == 2:  # Ensure each row has exactly two columns
            data.append((cleaned_row[0], cleaned_row[1]))

# Function to search based on user query
def search_specifications(query, data, model):
    query_embedding = model.encode([query])[0].reshape(1, -1)
    similarities = []
    for (path, description) in data:
        description_embedding = model.encode([description])[0].reshape(1, -1)
        similarity = cosine_similarity(query_embedding, description_embedding)[0][0]
        similarities.append((similarity, path, description))

    # Sort results by similarity in descending order
    similarities.sort(key=lambda x: x[0], reverse=True)
    return similarities

# Example search with a natural language query
specifications = "Need a pleated filter with polyethersulfone membrane that can handle temperatures of up to 75 degrees celsius. Diameter should be 2.75 inch. Should contain a gasket adapter."
matching_docs = search_specifications(specifications, data, model)

# Print results
if matching_docs:  # Check if there are matching documents
    max_similarity, max_path, max_description = max(matching_docs, key=lambda x: x[0])  # Get the tuple with maximum similarity
    print(f"Path: {max_path}\nDescription: {max_description}\nSimilarity: {max_similarity}\n")
else:
    print("No matching documents found.")  # Print a message if no matching documents were found

