# from Functions.PDF_Loader import reader_function
# from Functions.chunker import chunk_text
# from Functions.embedding_generation import embedder
from Functions.storing_function_VDB import storing_into_vectorDB
from Functions.storing_function_VDB import check_for_collection
from Functions.Querior_Processor import query_processor
from Functions.Ollama_LLM import generate_answer
from Functions.prompt_builder import build_prompt

path = input("Enter the path: ")
condition = True

print("="*120)
print("✅ All imports successful!")
print("="*120)

if not (check_for_collection(path)):
    condition = False
    print("The file's context is not there in the database, we will add the context to the databse.")
    print("="*120)


    vector_db_collection = storing_into_vectorDB(condition, path)
    print("="*120)
else:
    vector_db_collection = storing_into_vectorDB(condition, file_path = path)


processed_query = query_processor()
print("="*120)
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
print("✅ A response from the Local LLM has been generated")
print("="*120)