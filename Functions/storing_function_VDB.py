import chromadb
import os
import streamlit as st
from Functions.embedding_generation import embedder
from Functions.chunker import chunk_text
from Functions.PDF_Loader import reader_function
from Functions.chunker import chunk_text
from Functions.embedding_generation import embedder
# file_path = ""

def check_for_collection_in_database(file):

    answer = False
    
    client = chromadb.PersistentClient(path = "Chroma_Database")
    all_collections = client.list_collections()
    for collection in all_collections:
        print(collection.name)
        if (collection.name == f"{file[1]}_collection"):
            answer = True
            break
    
    return answer

def storing_collection_into_database(condition,
                    file
                    ):
    
    client = chromadb.PersistentClient(path = "Chroma_Database")
    
    if (condition == False):
        retrieved_information = file[0] 


        print("✅ The document's content has been retrieved")
        print("="*120)

        print(retrieved_information)
        print("="*120)
        chunks_from_retrieved_information = chunk_text(retrieved_information)
        print("✅ The document's content has been chunked down")
        print("="*120)

        print(chunks_from_retrieved_information)
        print("="*120)


        print("✅ The document's chunks has been embedded")
        embeddings = embedder(chunks_from_retrieved_information)
        print("="*120)
        print("✅ The embeddings has been stored in vector db")
    else:
        print("✅ The file's collection is already in the database. Directly continuing with the retrieval.")
        print("="*120)


    # if (condition):
    #     collection = client.get_collection(f"{file[1]}_collection")
    #     collection = collection
    # else:
    #     collection = client.create_collection(f"{file[1]}_collection")
    
    #     collection = collection 
    #     collection.add(
    #     documents=chunks_from_retrieved_information,
    #     embeddings=embeddings.tolist(),  # Converts your NumPy array to a Python list
    #     ids=[f"chunk_{i}" for i in range(len(chunks_from_retrieved_information))]
    #     )
    #     print(condition)

    if (check_for_collection_in_database(file) == False):

        # create the collection, else dont create the collection --> we do get_collection in both the cases.
        # case 1: the file is not there: we create then we do get_collection.
        # case 2: the file is there, so we only do get_collection.

        collection = client.create_collection(f"{file[1]}_collection")
        collection = collection
        collection.add(
        documents=chunks_from_retrieved_information,
        embeddings=embeddings.tolist(),  # Converts your NumPy array to a Python list
        ids=[f"chunk_{i}" for i in range(len(chunks_from_retrieved_information))]
        )

    collection = client.get_collection(f"{file[1]}_collection")

    return collection