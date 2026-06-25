from Functions.embedding_generation import embedder

def query_processor_and_results():

    query = input("Ask your question related to the document: ")

    processed_query = embedder(query)

    return [processed_query, query]