import os
import hashlib
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from utils.pdf_loader import load_pdf_chunks

# Load API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

PDF_PATH = "data/example.pdf"
VECTOR_DB_PATH = "vector_store/faiss_index"
HASH_PATH = os.path.join(VECTOR_DB_PATH, "source.hash")

def get_file_hash(file_path):
    """Returns SHA256 hash of a file (used to detect changes)"""
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def build_or_load_vector_db(chunks):
    """Load FAISS if index + PDF match, else rebuild index."""
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    index_file = os.path.join(VECTOR_DB_PATH, "index.faiss")
    current_hash = get_file_hash(PDF_PATH)

    # Check if index and hash match
    if os.path.exists(index_file) and os.path.exists(HASH_PATH):
        with open(HASH_PATH, "r") as f:
            saved_hash = f.read().strip()
        if saved_hash == current_hash:
            return FAISS.load_local(
                VECTOR_DB_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )

    # Rebuild FAISS index and save new hash
    db = FAISS.from_texts(chunks, embeddings)
    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    db.save_local(VECTOR_DB_PATH)
    with open(HASH_PATH, "w") as f:
        f.write(current_hash)
    return db

def get_qa_chain():
    """Return ready-to-use RetrievalQA chain."""
    chunks = load_pdf_chunks(PDF_PATH)
    vector_db = build_or_load_vector_db(chunks)
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})

    llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )
    return qa_chain
