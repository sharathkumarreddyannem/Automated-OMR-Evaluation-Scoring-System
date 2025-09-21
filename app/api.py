from fastapi import FastAPI, UploadFile, File
import shutil
import os
from omr.pipeline import evaluate_sheet

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = evaluate_sheet(file_path)
    return {"filename": file.filename, "results": results}
