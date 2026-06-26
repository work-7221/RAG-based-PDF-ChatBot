import chromadb
import os


def storing_into_vectorDB(embeddings, chunks, file_path):
    client = chromadb.PersistentClient(path = "Chroma_Database")

    collection = client.get_or_create_collection(f"{os.path.basename(file_path)}_collection")
    
    collection.add(
    documents=chunks,
    embeddings=embeddings.tolist(),  # Converts your NumPy array to a Python list
    ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

    return collection