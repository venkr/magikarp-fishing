import json
import os
import numpy as np

# Read all files of form cl100k_base_embeddings_*.json

files = os.listdir('embeds')
files = [f for f in files if f.startswith('cl100k_base_embeddings_') and f.endswith('.json')]

combined_embeddings = {} # token -> embedding

for f in files:
    with open("embeds/" + f, 'r') as f:
        combined_embeddings.update(json.load(f))

# print the length of the first embedding
print(len(list(combined_embeddings.values())[0]))
# 1536

# initialize a 1d np array to all zeroes of length 1536
accumulator = np.zeros(1536)

# add all embeddings together
for embedding in combined_embeddings.values():
    accumulator += np.array(embedding)

# divide by the number of embeddings
accumulator /= len(combined_embeddings)

# order the embeddings by their cosine distance from the average embedding
# also store the cosine distance in the tuple

ordered_embeddings = map(lambda x: (x[0], x[1], np.dot(x[1], accumulator) / (np.linalg.norm(x[1]) * np.linalg.norm(accumulator))), combined_embeddings.items())
ordered_embeddings = sorted(ordered_embeddings, key=lambda x: x[2], reverse=True)

# print the first 100 tokens
for token, embedding, distance in ordered_embeddings[:100]:
    print(token, distance)