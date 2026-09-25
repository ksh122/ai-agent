from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""],
    length_function=len,
    is_separator_regex=False,
)

ROOT = Path(__file__).resolve().parent.parent
document_path = ROOT / "uploaded_documents" / "e6477efa-cfbd-4b52-817d-6b168513e1f0.txt"

text = document_path.read_text(encoding="utf-8")

chunks = text_splitter.split_text(text)

print(f"chunks: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
    print("-"*100)



