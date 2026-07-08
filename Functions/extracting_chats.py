from pathlib import Path

CHAT_DIR = Path(
    r"C:\My_Folder_Rohan\Rohan\Hell_Yeah\Personal_Projects\RAG based PDFChatBot\Chat_History"
)

# extracting chats from the file object 
def extract_chats(name):
    

    file_path = CHAT_DIR / f"{name}.txt"

    if not file_path.exists():
        return ""

    return file_path.read_text(encoding="utf-8")