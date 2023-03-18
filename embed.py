import tiktoken
import openai
import asyncio
from aiohttp import ClientSession
import json
import time

#openai.api_key = "YOUR_API_KEY"

# read the cl100k_base embeddings 
cl100k_base = tiktoken.get_encoding("cl100k_base")

# print some tokens
for i in range(cl100k_base.n_vocab):
    if i % 1000 == 0:
        print(cl100k_base.decode([i]))

async def get_embedding(text, model="text-embedding-ada-002"):
    resp = await openai.Embedding.acreate(input = [text], model=model)
    return resp['data'][0]['embedding']

async def main():
    openai.aiosession.set(ClientSession())
    for i in range(92000, cl100k_base.n_vocab, 1000):
        tasks = []
        tokens = []
        
        tokens = [cl100k_base.decode([j]) for j in range(i, min(i+1000, cl100k_base.n_vocab))]
        tasks = [get_embedding(token) for token in tokens]
        embeddings = await asyncio.gather(*tasks)
  
        with open(f'embeds/cl100k_base_embeddings_{i}.json', 'w') as f:
            json.dump(dict(zip(tokens, embeddings)), f)

        time.sleep(20)  
    await openai.aiosession.get().close()

asyncio.run(main())