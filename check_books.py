from pathlib import Path
import PyPDF2

BOOKS_FOLDER = Path.home() / "ALL_DATA_BACKUP"

for file in BOOKS_FOLDER.glob("*.pdf"):
    reader = PyPDF2.PdfReader(str(file))
    print(file.name, "has", len(reader.pages), "pages")
