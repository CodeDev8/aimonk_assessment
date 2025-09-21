import shutil
import uuid
from os import environ
from pathlib import Path

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from requests import post

app = FastAPI()

AI_BACKEND_HOST = environ.get("AI_BACKEND_HOST", "localhost")
AI_BACKEND_PORT = environ.get("AI_BACKEND_PORT", "8001")
DETECT_ENDPOINT = f"http://{AI_BACKEND_HOST}:{AI_BACKEND_PORT}/detect"

TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(parents=True, exist_ok=True)


@app.post("/detect")
async def detect(image: UploadFile = File(...)):
    temp_filename = f"temp_{uuid.uuid4().hex}_{image.filename}"
    temp_path = TEMP_DIR / temp_filename

    with temp_path.open("wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    with temp_path.open("rb") as f:
        detection_response = post(
            DETECT_ENDPOINT,
            files={"image": (image.filename, f, image.content_type)},
        )

    temp_path.unlink(missing_ok=True)

    return JSONResponse(content=detection_response.json())
