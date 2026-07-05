import uuid
from pathlib import Path




# This function takes chat relative path location, the chat content and stores it in a file.
def update_chats(name, chat_content):
    dir_path = Path(r"C:\My_Folder_Rohan\Rohan\Hell_Yeah\Personal_Projects\RAG based PDFChatBot\Chat_History")

    file_path = dir_path / f"{name}.txt"

    if file_path.is_file() is False:
        file_path.write_text("Starting a chat history...", encoding = "utf-8")
        file_path.write_text(chat_content)
    else:
        with file_path.open(mode = "w", encoding = "utf-8") as file:
            file.write(chat_content)


# storing_chats("f1.txt", "UPDATE! IT WORKS!")