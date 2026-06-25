from Functions.PDF_Loader import reader_function
from Functions.chunker import chunk_text
from Functions.embedding_generation import embedder
from Functions.storing_function_VDB import storing_into_vectorDB
from Functions.Querior_Processor import query_processor
from Functions.Ollama_LLM import generate_answer
from Functions.prompt_builder import build_prompt

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
print("="*120)


print("✅ The document's chunks has been embedded")
embeddings = embedder(chunks_from_retrieved_information)
print("="*120)
print("✅ The embeddings has been stored in vector db")

vector_db_collection = (storing_into_vectorDB(embeddings, chunks_from_retrieved_information))
print("="*120)

processed_query = query_processor()
print("✅ A query has been asked from the user and has been processed.")
print("="*120)

compared_results = vector_db_collection.query(
    query_embeddings=processed_query[0].tolist(),
    n_results=3
)

context = "\n\n".join(compared_results["documents"][0])


answer_to_query = generate_answer(build_prompt(processed_query[1], context))
print("✅ The query has been send to the LLM with the context from the provided knowledge base.")
print(answer_to_query)
print("="*120)
print("✅ A response from the Local LLM has been geenrated")
print("="*120)