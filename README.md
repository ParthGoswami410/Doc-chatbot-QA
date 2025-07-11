
# 📘 README

## ✅ Setup + Run Instructions

### 1. Clone the Repository & Setup Environment
```bash
git clone https://github.com/your-username/docbot.git
cd docbot
python -m venv venv
venv\Scripts\activate     
pip install -r requirements.txt
```

### 2. Create `.env` File
Create a `.env` file in the root directory with your Groq API key:
```
GROQ_API_KEY=your_groq_api_key
```

### 3. Run the Flask App
```bash
python main.py
```

### 4. Run the Demo Notebook
Open `demo_script.ipynb` and execute:
- Folder uploaded_docs
- 3 question tests
- View chatbot answers with citations

---

## 🧱 Architecture Overview Diagram

```
       ┌──────────────┐
       │  Documents   │
       └──────┬───────┘
              │
       ┌──────▼──────┐
       │  Parser     │  ← Extracts clean text
       └──────┬──────┘
              │
       ┌──────▼──────┐
       │ Embedder    │  ← Embeds chunks via SentenceTransformers
       └──────┬──────┘
              │
       ┌──────▼──────┐
       │ Retriever   │  ← Top-k semantic search
       └──────┬──────┘
              │
       ┌──────▼──────┐
       │ Generator   │  ← LLM generates answer w/ citations
       └─────────────┘
```

---

## 🧠 Description of How It Works

### 🔹 Embedding
- Documents are parsed and chunked.
- Embeddings are generated using `sentence-transformers`.

### 🔹 Retrieval
- User question is embedded.
- Cosine similarity is used to retrieve top-k most relevant chunks.

### 🔹 Generation
- Retrieved chunks and question are sent to a Groq-powered LLM (e.g., LLaMA 3).
- Answer is generated (≤ 500 words) with inline citations:  
 


