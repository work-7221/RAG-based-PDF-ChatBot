from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(all_text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(all_text)

    return chunks