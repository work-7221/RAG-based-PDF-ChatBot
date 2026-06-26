import chromadb
import os
from Functions.embedding_generation import embedder
from Functions.chunker import chunk_text

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
    chunks = chunk_text(file_path)
    embeddings = embedder(file_path)
    
    client = chromadb.PersistentClient(path = "Chroma_Database")
    if (condition == False):
        collection = client.create_collection(f"{os.path.basename(file_path)}_collection")
    
        collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),  # Converts your NumPy array to a Python list
        ids=[f"chunk_{i}" for i in range(len(chunks))]
        )
    else:
        collection = client.get_collection(f"{os.path.basename(file_path)}_collection")

    return collection