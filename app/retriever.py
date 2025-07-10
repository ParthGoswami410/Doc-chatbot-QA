import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL, VECTOR_DB_PATH, METADATA_STORE_PATH, TOP_K

model = SentenceTransformer(EMBEDDING_MODEL)

def retrieve_relevant_chunks(query):
    index = faiss.read_index(VECTOR_DB_PATH)
    with open(METADATA_STORE_PATH, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    query_embedding = model.encode(query).astype('float32').reshape(1, -1)
    _, indices = index.search(query_embedding, TOP_K)

    results = []
    for idx in indices[0]:
        results.append(metadata[idx])
    return results
