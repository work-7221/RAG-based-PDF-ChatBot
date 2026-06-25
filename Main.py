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


embeddings = embedder(chunks_from_retrieved_information)
print(len(chunks_from_retrieved_information))
print(len(embeddings))
print(type(embeddings))
print(embeddings.shape)

vector_db_collection = (storing_into_vectorDB(embeddings, chunks_from_retrieved_information))

processed_query = query_processor()

compared_results = vector_db_collection.query(
    query_embeddings=processed_query[0].tolist(),
    n_results=3
)
print(compared_results)

context = "\n\n".join(compared_results["documents"][0])


answer_to_query = generate_answer(build_prompt(processed_query[1], context))
print(answer_to_query)