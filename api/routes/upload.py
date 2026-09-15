from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
import uuid

router = APIRouter(
    prefix="/upload",
    tags=["File Upload"]
)


@router.post("/")
def upload_file(file: UploadFile = File(...)):

    # 1. Check file type
    allowed_types = [
        "image/jpeg",
        "image/png"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, JPEG and PNG images are allowed"
        )

    # 2. Check file size
    MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB

    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)

    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size must be less than 2 MB"
        )

    # 3. Create upload folder
    upload_folder = "uploads/employees"

    os.makedirs(upload_folder, exist_ok=True)

    safe_filename = os.path.basename(file.filename)
    unique_filename = f"{uuid.uuid4()}_{file.filename}"

    # 4. Create file path
    file_path = os.path.join(
        upload_folder,
        unique_filename
    )

    # 5. Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File uploaded successfully"
    }

    