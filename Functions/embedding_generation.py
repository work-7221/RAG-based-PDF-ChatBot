from sentence_transformers  import SentenceTransformer 

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def embedder(chunks):
    embeddings = model.encode(chunks)
    return embeddings