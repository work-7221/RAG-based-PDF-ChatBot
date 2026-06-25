import chromadb

def storing_into_vectorDB(embeddings, chunks):
    client = chromadb.Client()

    collection = client.create_collection("MyVectorDataBase")
    
    collection.add(
    documents=chunks,
    embeddings=embeddings.tolist(),  # Converts your NumPy array to a Python list
    ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

    return collection