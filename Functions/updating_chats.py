import uuid
from pathlib import Path


CHAT_DIR = Path(
    r"C:\My_Folder_Rohan\Rohan\Hell_Yeah\Personal_Projects\RAG based PDFChatBot\Chat_History"
)

# This function takes chat relative path location, the chat content and stores it in a file.
def update_chats(name, chat_content):
    CHAT_DIR.mkdir(exist_ok=True)

    file_path = CHAT_DIR / f"{name}.txt"

    file_path.write_text(
        chat_content,
        encoding="utf-8"
    )


# storing_chats("f1.txt", "UPDATE! IT WORKS!")