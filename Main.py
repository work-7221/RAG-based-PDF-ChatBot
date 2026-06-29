# from Functions.PDF_Loader import reader_function
# from Functions.chunker import chunk_text
# from Functions.embedding_generation import embedder
import streamlit as st
from Functions.storing_function_VDB import storing_collection_into_database
from Functions.storing_function_VDB import check_for_collection_in_database
from Functions.Querior_Processor import query_processor
from Functions.Ollama_LLM import generate_answer
from Functions.prompt_builder import build_prompt


def Main_Functionality(PDF_content_from_streamlit, query):

    print("="*120)
    print("✅ All imports successful!")
    print("="*120)

    context = ""

    file = PDF_content_from_streamlit
    processed_query = query_processor(query)
    condition = True
    if file is not None:

        if (check_for_collection_in_database(f"{file[1]}_collection")):

            condition = False

            print("The file's context is not there in the database, we will add the context to the database.")

            print("="*120)

            vector_db_collection = storing_collection_into_database(condition, file)

            print("="*120)

            compared_results = vector_db_collection.query(
                query_embeddings=processed_query[0].tolist(),
                n_results=3
            )

            context = "\n\n".join(compared_results["documents"][0])

        else:
            vector_db_collection = storing_collection_into_database(condition, file)

            compared_results = vector_db_collection.query(
                query_embeddings=processed_query[0].tolist(),
                n_results=3
            )

            context = "\n\n".join(compared_results["documents"][0])



    print("="*120)
    print("✅ A query has been asked from the user and has been processed.")
    print("="*120)



    answer_to_query = generate_answer(build_prompt(processed_query[1], context))

    print("✅ The query has been sent to the LLM with the context from the provided knowledge base.")

    print(answer_to_query)

    print("="*120)
    print("✅ A response from the Local LLM has been generated")
    print("="*120)

    return answer_to_query