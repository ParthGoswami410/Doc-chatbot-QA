import openai
from app.config import TOP_K
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# You should set your OpenAI key as env var or .env
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(query, retrieved_chunks):
    context = ""
    citations = []

    for chunk in retrieved_chunks:
        context += chunk["chunk"] + "\n"
        citations.append(f"[{chunk['doc']}, chunk {chunk['chunk_id']}]")

    prompt = (
        f"Answer the question based on the context below.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n"
        f"Answer in under 500 words. If not found, say 'I don’t know'.\n"
        f"Include inline citations like [filename, chunk#]."
    )

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful  assistant."},
            {"role": "user", "content": prompt}
        ]
    )


    return response.choices[0].message.content

