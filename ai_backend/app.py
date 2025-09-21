import uuid
from pathlib import Path

from detector import run_detection
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/detect")
async def detect(image: UploadFile = File(...)):
    temp_filename = f"upload_{uuid.uuid4().hex}_{image.filename}"
    temp_path = Path("/tmp") / temp_filename

    with temp_path.open("wb") as buffer:
        buffer.write(await image.read())

    json_data = run_detection(input_path=str(temp_path))

    temp_path.unlink(missing_ok=True)

    return JSONResponse(content=json_data)
