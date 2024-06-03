import pymupdf
import os

def extract_text_from_pdf(pdf_path):
    document = pymupdf.open(pdf_path)
    title = document.metadata['title']
    if not title:
        title = os.path.splitext(os.path.basename(pdf_path))[0]  # Use file name as title if no title in metadata
    
    safe_title = "".join(x for x in title if x.isalnum() or x in " -_").strip()
    filename = f"{safe_title}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        for page in document:
            text = page.get_text()
            f.write(text)
    
    print(f"Content extracted and saved to {filename}")

def process_all_pdfs(directory):
    # Loop through all files in the provided directory
    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            extract_text_from_pdf(pdf_path)

# Example usage
current_directory = '.'  # '.' means current directory
process_all_pdfs(current_directory)
