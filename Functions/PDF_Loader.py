from pypdf import PdfReader

def reader_function(PDF_path):
    pages = ''
    reader = PdfReader(PDF_path)

    total_pages = len(reader.pages)
    
    for i in range(total_pages):

        page = reader.pages[i]
        pages += page.extract_text()


    return pages