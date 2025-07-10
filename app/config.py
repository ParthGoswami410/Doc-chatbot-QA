import os

UPLOAD_FOLDER = 'uploaded_docs'
CHUNK_SIZE = 500  # characters
TOP_K = 3         # top-k relevant chunks for answering

EMBEDDING_MODEL = 'all-MiniLM-L6-v2'  # HuggingFace SentenceTransformer
VECTOR_DB_PATH = 'vector_store.faiss'
METADATA_STORE_PATH = 'metadata.json'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
