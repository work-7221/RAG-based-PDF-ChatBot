from pypdf import PdfReader

def reader_function(PDF_path):
    pages = []
    reader = PdfReader(PDF_path)

    total_pages = len(reader.pages)

    for i in range(total_pages):

        text = reader.pages[i];

        print("="*40)
        print(f"This is Page Number {i} with content: ")
        print(text.extract_text())
        pages.append(text.extract_text())


    return pages 