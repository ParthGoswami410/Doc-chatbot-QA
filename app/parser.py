import os
import PyPDF2
import markdown
from app.config import UPLOAD_FOLDER

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_text_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = markdown.markdown(f.read())
        return html  # Optional: strip tags if needed

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ''
    return text

def extract_text(file_path):
    if file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    elif file_path.endswith('.md'):
        return extract_text_from_md(file_path)
    elif file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file format")

def load_documents(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith(('.pdf', '.txt', '.md')):
            text = extract_text(file_path)
            documents.append({
                'filename': filename,
                'text': text
            })
    return documents
