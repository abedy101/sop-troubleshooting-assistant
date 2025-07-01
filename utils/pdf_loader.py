from PyPDF2 import PdfReader

def load_pdf_chunks(pdf_path, chunk_size=1000, overlap=200):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    
    # Chunk text with overlap
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks

