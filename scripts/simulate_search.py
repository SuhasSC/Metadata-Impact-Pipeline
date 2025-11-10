import pandas as pd
import random
import os

# Load the CSV data
df = pd.read_csv("data/raw_documents.csv")

# Simulate search queries (random keywords from tags or description)
search_keywords = ['AI', 'healthcare', 'education', 'cybersecurity', 'energy', 'agriculture', 'NLP']

# Store results
results = []

# Simulate 5 searches
for i in range(5):
    query = random.choice(search_keywords)
    
    # Simple search: match in title or description
    matches = df[df['title'].str.contains(query, case=False) | df['description'].str.contains(query, case=False)]
    
    if not matches.empty:
        top_doc = matches.iloc[0]
        result = {
            "query": query,
            "title": top_doc['title'],
            "description": top_doc['description'],
            "tags": top_doc['tags'],
            "metadata_quality": top_doc.get('metadata_quality', 'N/A'),
            "impact_score": top_doc.get('impact_score', 'N/A')
        }
        results.append(result)

# Create results folder if not exists
os.makedirs("results", exist_ok=True)

# Save results to CSV
pd.DataFrame(results).to_csv("results/search_simulation_results.csv", index=False)

# Print completion message
print("Search simulation complete. Results saved to results/search_simulation_results.csv")
