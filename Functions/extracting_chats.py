from pathlib import Path


# extracting chats from the file object 
def extract_chats(name):
    
    dir_path = Path(r"C:\My_Folder_Rohan\Rohan\Hell_Yeah\Personal_Projects\RAG based PDFChatBot\Chat_History")

    file_path = dir_path / f"{name}.txt"

    text = None

    if file_path.is_file():
        text = file_path.read_text(encoding="utf-8")

    return text