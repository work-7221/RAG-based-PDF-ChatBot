import streamlit as st
from Functions.embedding_generation import embedder

def query_processor(query):

    processed_query = embedder(query)

    return [processed_query, query]