import chromadb
import os
from Functions.embedding_generation import embedder
from Functions.chunker import chunk_text
from Functions.PDF_Loader import reader_function
from Functions.chunker import chunk_text
from Functions.embedding_generation import embedder
file_path = ""

def check_for_collection(file_path):
    client = chromadb.PersistentClient(path = "Chroma_Database")
    all_collections = client.list_collections()
    for collection in all_collections:
        if (collection.name == f"{os.path.basename(file_path)}_collection"):
            return True
    
    file_path = file_path

    return False

def storing_into_vectorDB(condition,
                          file_path,
                          ):
    if (condition == False):
        retrieved_information = reader_function(file_path)
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
    else:
        print("✅ The file's collection is already in the database. Directly continuing with the retrieval.")
        print("="*120)

    client = chromadb.PersistentClient(path = "Chroma_Database")

    if (condition == True):
        collection = client.get_collection(f"{os.path.basename(file_path)}_collection")
    else:
        collection = client.create_collection(f"{os.path.basename(file_path)}_collection")
    
        collection.add(
        documents=chunks_from_retrieved_information,
        embeddings=embeddings.tolist(),  # Converts your NumPy array to a Python list
        ids=[f"chunk_{i}" for i in range(len(chunks_from_retrieved_information))]
        )

    return collection