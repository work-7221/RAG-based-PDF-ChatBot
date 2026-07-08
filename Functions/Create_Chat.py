from pathlib import Path

CHAT_DIR = Path(r"C:\My_Folder_Rohan\Rohan\Hell_Yeah\Personal_Projects\RAG based PDFChatBot\Chat_History")

def create_chat(chat_name):

    file = CHAT_DIR / f"{chat_name}.txt"

    if file.exists():
        return False

    file.write_text("[]", encoding="utf-8")

    return True