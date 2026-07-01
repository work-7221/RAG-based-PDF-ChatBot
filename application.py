import streamlit as st
# import Testing
from Main import Main_Functionality
from Functions.PDF_Loader import reader_function
import subprocess as sb

path_to_ipex_directory = r"C:\Users\work_\IPEX_OLLAMA"
process = sb.Popen(
    'start-ollama',
    cwd = path_to_ipex_directory,
    text = True,    
    shell = True
)
process.wait()

@st.fragment
def application_fragment():
    st.title("📚RAG based PDF Chatbot")

    # 1. Dedicated RAG logic placeholder
    def run_rag_pipeline(user_query):
        # --- INSERT YOUR RAG LOGIC HERE ---
        # 1. Vector search: docs = vector_store.similarity_search(user_query)
        # 2. LLM Generation: response = llm.invoke(docs + user_query)

            
        answer = Main_Functionality(uploaded_file, user_query)
        return answer

    # 2. Initialize memory
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 3. Render chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # 4. If needed, get the required document.
    uploaded_file = st.file_uploader("Upload your PDF document", type = ["PDF"])
    if (uploaded_file != None):
            # st.write(type(uploaded_file))
            uploaded_file = [reader_function(uploaded_file), uploaded_file.name]

    # 5. Handle new user input
    if prompt := st.chat_input("Ask a question about your data..."):
        # Show and save user prompt
        st.chat_message("user").write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Run your RAG pipeline
        answer = run_rag_pipeline(prompt)
        
        # Show and save assistant response
        st.chat_message("assistant").write(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

application_fragment()