from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path
from uuid import uuid4

app = FastAPI()

UPLOAD_DIR = Path("uploaded_documents")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith((".txt",".md")):
        raise HTTPException(
            status_code=400,
            detail="File must end with .txt or .md"
        )
    
    document_id = str(uuid4())
    extension = Path(file.filename).suffix
    file_path = UPLOAD_DIR / f"{document_id}{extension}"

    content = await file.read()
    file_path.write_bytes(content)
    text_content = content.decode("utf-8")

    return {
        "document_id": document_id,
        "filename": file.filename,
        "text_length": len(text_content),
        "message": "File uploaded successfully."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("file_upload:app", host="127.0.0.1", port=8000, reload=True)