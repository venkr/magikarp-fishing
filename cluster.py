import json
import os
import numpy as np
from sklearn.cluster import KMeans

# Read all files of form cl100k_base_embeddings_*.json

files = os.listdir('embeds')
files = [f for f in files if f.startswith('cl100k_base_embeddings_') and f.endswith('.json')]

combined_embeddings = {} # token -> embedding

for f in files:
    with open("embeds/" + f, 'r') as f:
        combined_embeddings.update(json.load(f))

# cluster the embeddings into 20 clusters using k-means clustering, and
# display 10 random tokens from each cluster

# downsample to 10%
combined_embeddings = {token: embedding for token, embedding in combined_embeddings.items() if np.random.random() < 0.1}

kmeans = KMeans(n_clusters=20, random_state=0).fit(list(combined_embeddings.values()))
for i in range(20):
    print(f"Cluster {i}")
    print(" ".join([token for token, cluster in zip(combined_embeddings.keys(), kmeans.labels_) if cluster == i][:10]))
    print()