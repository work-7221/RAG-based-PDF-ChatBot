from sentence_transformers import SentenceTransformer
import chromadb
from pypdf import PdfReader
import ollama

from Functions import PDF_Loader


print("="*40)
print("All imports successful!")
print("="*40)


print(PDF_Loader.reader_function("PDFs/research_upperBody.pdf"))
