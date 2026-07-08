import streamlit as st
from pathlib import Path
from Functions.Create_Chat import create_chat

st.title("Chats")

if "creating_chat" not in st.session_state:
    st.session_state.creating_chat = False

if st.button("➕ New Chat", use_container_width=True):
    st.session_state.creating_chat = True

if st.session_state.creating_chat:

    chat_name = st.text_input(
        "Conversation Name",
        placeholder="e.g. Machine Learning"
    )

    if st.button("Create"):

        success = create_chat(chat_name)

        if success:

            st.session_state.selected_chat = chat_name
            st.session_state.creating_chat = False

            st.switch_page("application.py")

        else:
            st.error("A chat with that name already exists.")

CHAT_DIR = Path(
    r"C:\My_Folder_Rohan\Rohan\Hell_Yeah\Personal_Projects\RAG based PDFChatBot\Chat_History"
)

if "selected_chat" not in st.session_state:
    st.session_state.selected_chat = None

st.subheader("Previous Chats")

for chat in sorted(CHAT_DIR.glob("*.txt")):

    chat_name = chat.stem

    if st.button(chat_name, use_container_width=True):

        st.session_state.selected_chat = chat_name

        st.switch_page("application.py")