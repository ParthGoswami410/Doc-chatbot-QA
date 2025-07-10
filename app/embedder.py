import json
import faiss
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from app.helpers import chunk_text
from app.config import EMBEDDING_MODEL, VECTOR_DB_PATH, METADATA_STORE_PATH, CHUNK_SIZE

model = SentenceTransformer(EMBEDDING_MODEL)

def build_embeddings(documents):
    vectors = []
    metadata = []

    for doc in tqdm(documents, desc="Embedding"):
        chunks = chunk_text(doc['text'], CHUNK_SIZE)
        for i, chunk in enumerate(chunks):
            embedding = model.encode(chunk)
            vectors.append(embedding)
            metadata.append({
                "doc": doc['filename'],
                "chunk": chunk,
                "chunk_id": i
            })

    vectors_np = np.array(vectors).astype('float32')

    # Save to FAISS
    index = faiss.IndexFlatL2(vectors_np.shape[1])
    index.add(vectors_np)
    faiss.write_index(index, VECTOR_DB_PATH)

    # Save metadata
    with open(METADATA_STORE_PATH, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)
