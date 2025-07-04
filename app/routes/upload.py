
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/")
def upload_document(file: UploadFile = File(...)):
    return {"filename": file.filename, "status": "uploaded"}
