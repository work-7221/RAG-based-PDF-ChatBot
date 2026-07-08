import streamlit as st

page_history = st.Page(
    "Chat_History_Selection.py",
    title="Chats"
)

page_chat = st.Page(
    "application.py",
    title="Application"
)

pg = st.navigation(
    [page_history, page_chat],
    position="hidden"
)

pg.run()