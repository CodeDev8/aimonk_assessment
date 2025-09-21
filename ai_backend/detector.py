from pathlib import Path
from time import time
from typing import Any, Dict, List, Tuple

import torch
from PIL import Image

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

model: torch.nn.Module = torch.hub.load(
    "ultralytics/yolov5", "yolov5s", pretrained=True
)

if torch.cuda.is_available():
    model.to("cuda")
else:
    model.to("cpu")


def run_detection(input_path: str) -> Tuple[Any, Dict[str, List[Dict[str, Any]]]]:
    results = model(input_path)
    rendered_images = results.render()
    saved_files = []
    for i, img in enumerate(rendered_images):
        filename = f"output_{int(time())}_{i}.jpg"
        out_path = OUTPUT_DIR / filename
        Image.fromarray(img).save(out_path)
        saved_files.append(str(filename))

    detections: List[Dict[str, Any]] = (
        results.pandas().xyxy[0].to_dict(orient="records")
    )
    json_data: Dict[str, List[Dict[str, Any]]] = {
        "detections": detections,
        "saved_files": saved_files,
    }

    return json_data
