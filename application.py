import streamlit as st
import subprocess as sb
from Main import Main_Functionality
from Functions.PDF_Loader import reader_function
from Functions.extracting_chats import extract_chats
from Functions.updating_chats import update_chats
import ast

if ("ollama_started" not in st.session_state):

    path_to_ipex_directory = r"C:\Users\work_\IPEX_OLLAMA"
    process = sb.Popen(
        'start-ollama',
        cwd = path_to_ipex_directory,
        text = True,
        shell = True
    )
    process.wait()

    st.session_state.ollama_started = True

with st.sidebar:
    if st.button("← Chats", use_container_width=True):
        st.switch_page("Chat_History_Selection.py")

# @st.fragment
# def application_fragment():
st.title("📚RAG based PDF Chatbot")

if "selected_chat" not in st.session_state:
    st.warning("Please select a chat first.")
    st.stop()

chat_name = st.session_state.selected_chat

if (
    "loaded_chat" not in st.session_state
    or st.session_state.loaded_chat != chat_name
):

    chat_data = extract_chats(chat_name)

    if chat_data:
        st.session_state.messages = ast.literal_eval(chat_data)
    else:
        st.session_state.messages = []

    st.session_state.loaded_chat = chat_name


ongoing_context = st.session_state.messages
print(ongoing_context)

# 3. Render chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


# this stops reader_function (full pdf text extraction)
# from rerunning on every chat message; it only runs again if the uploaded file actually changes.
uploaded_file_raw = st.file_uploader("Upload your PDF document", type = ["PDF"])
if (uploaded_file_raw != None):
        file_key = f"{uploaded_file_raw.name}_{uploaded_file_raw.size}"
        if st.session_state.get("processed_file_key") != file_key:
            st.session_state.processed_pdf_text = reader_function(uploaded_file_raw)
            st.session_state.processed_file_key = file_key
        uploaded_file = [st.session_state.processed_pdf_text, uploaded_file_raw.name]
else:
        uploaded_file = None

# 1. Dedicated RAG logic placeholder
def run_rag_pipeline(user_query):
    # --- INSERT YOUR RAG LOGIC HERE ---
    # 1. Vector search: docs = vector_store.similarity_search(user_query)
    # 2. LLM Generation: response = llm.invoke(docs + user_query)

        
    answer = Main_Functionality(uploaded_file, user_query, ongoing_context)
    return answer

# 2. Initialize memory

# 4. If needed, get the required document.

# 5. Handle new user input
prompt = st.chat_input("Ask a question about your data...")
if prompt:
    # Show and save user prompt
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Run your RAG pipeline
    answer = run_rag_pipeline(prompt)
    
    # Show and save assistant response
    st.chat_message("assistant").write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

    update_chats(chat_name, str(st.session_state.messages))
# application_fragment()