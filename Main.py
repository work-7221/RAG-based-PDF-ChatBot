from Functions.PDF_Loader import reader_function
from Functions.chunker import chunk_text

pages = reader_function("PDFs/research_upperBody.pdf")


print("="*120)
print("✅ All imports successful!")
print("="*120)


retrieved_information = reader_function("PDFs/research_upperBody.pdf")
chunks_from_retrieved_information = chunk_text(retrieved_information)


print("✅ The document's content has been retrieved")
print("="*120)

print(retrieved_information)
print("="*120)
print("✅ The document's content has been chunked down")
print("="*120)

print(chunks_from_retrieved_information)
print(len(chunks_from_retrieved_information))
print("="*120)


