import nltk
import numpy as np
from nltk.tokenize import sent_tokenize
from Functions.embedding_generation import model

from sklearn.metrics.pairwise import cosine_similarity
from langchain_text_splitters import RecursiveCharacterTextSplitter
# def chunk_text(all_text):
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=100
#     )

#     chunks = splitter.split_text(all_text)

#     return chunks
def chunk_text(text):

    # model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2") reloads a 2nd full model 

    sentences = sent_tokenize(text)
    embeddings = model.encode(sentences)

    # 1. Calculate all consecutive similarities
    similarities = []
    for i in range(len(embeddings) - 1):
        sim = cosine_similarity([embeddings[i]], [embeddings[i + 1]])
        similarities.append(sim)
        print(f"Sentence {i+1} ↔ Sentence {i+2}: {sim[0][0]:.4f}")

    # 2. Compute a dynamic threshold based on distances (1 - similarity)
    # Larger distance means a bigger topic shift
    distances = [1 - s for s in similarities]
    
    # Set threshold at the 80th percentile of distances (meaning top 20% biggest drops split the text)
    # For short texts, you can adjust this percentile target
    distance_threshold = np.percentile(distances, 80) 
    
    print(f"\nDynamic Distance Threshold for Splitting: {distance_threshold:.4f}")

    # 3. Form the chunks using the dynamic threshold
    chunks = []
    current_chunk = [sentences[0]]

    for i in range(len(distances)):
        if distances[i] > distance_threshold:
            # Distance is too big -> Cut here and start a new chunk
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentences[i + 1]]
        else:
            # Safe to merge
            current_chunk.append(sentences[i + 1])

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    smthing = []
    # Print evaluation
    print("\n=== Formed Semantic Chunks ===")
    for idx, chunk in enumerate(chunks, 1):
        # print(f"Chunk {idx}:\n{chunk}\n")
        smthing.append(f"chunk {idx}: {chunk}")

    print(chunks)

    return smthing