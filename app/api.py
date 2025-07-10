import os
from flask import Blueprint, request, jsonify
from app.parser import load_documents
from app.embedder import build_embeddings
from app.retriever import retrieve_relevant_chunks
from app.generator import generate_answer
from app.config import UPLOAD_FOLDER

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/upload', methods=['POST'])
def upload_docs():
    folder = request.form.get('folder_path')
    if not folder:
        return jsonify({"error": "No folder path provided"}), 400

    docs = load_documents(folder)
    build_embeddings(docs)

    return jsonify({"message": f"{len(docs)} documents processed."})

@api_blueprint.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    query = data.get("question", "")
    if not query:
        return jsonify({"error": "No question provided"}), 400

    chunks = retrieve_relevant_chunks(query)
    answer = generate_answer(query, chunks)
    return jsonify({"answer": answer})
