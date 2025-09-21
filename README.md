# AIMonk Technical Assessment Documentation

## Overview

This project implements a **microservice-based architecture** for an image object detection pipeline. It consists of three components:

1. **ai_backend** – Runs a lightweight object detection model (YOLOv5s / CPU compatible). Takes image input, performs inference, and outputs:
   - JSON with detected objects, bounding boxes, and confidence scores
   - Processed image with bounding boxes drawn

   Accessible via Swagger API after port forwarding (default port `8001`)

2. **ui_backend** – Acts as an interface layer between the AI backend and the frontend. It accepts image uploads from the frontend, forwards them to the AI backend, and returns results. Can also be accessed via Swagger API after port forwarding (default port `8002`)

3. **Streamlit App** – A user-facing interface that allows users to upload images, view the JSON as a table, and see the output image. Default endpoint `localhost:8003`

The services communicate using REST APIs and are containerized with Docker and orchestrated using Docker Compose.

---

## Architecture

```
[ User Uploads Image ] 
        ↓
   [ Streamlit UI ]
        ↓ REST API
   [ UI Backend ]
        ↓ REST API
   [ AI Backend (YOLOv5s) ]
        ↓
  ┌─────────────┬──────────────┐
  │ Processed   │ JSON Output  │
  │ Image       │ (objects,    │
  │ (with bboxes)│ confidence) │
  └─────────────┴──────────────┘
```

---

## Prerequisites

- Docker
- Docker Compose
- Linux

---

## Project Structure

```
aimonk/
│── ai_backend/         # AI backend service (YOLO model inference)
│── ui_backend/         # UI backend service (API gateway)
│── streamlit_app/      # Frontend Streamlit app
│── outputs/            # Stores processed images
│── docker-compose.yml  # Multi-service orchestration
```

---

## Setup & Running Instructions

After extracting the project folder zip, open a terminal inside the project directory and run:

```
docker-compose up --build
```

### Access Services

- **Streamlit App (Frontend):** [http://localhost:8003](http://localhost:8003)
- **UI Backend API Docs:** [http://localhost:8002/docs](http://localhost:8002/docs)
- **AI Backend API Docs:** [http://localhost:8001/docs](http://localhost:8001/docs)

### Using the App

1. Open the Streamlit UI.
2. Upload an image.
3. The app will display:
   - Processed image with bounding boxes
   - JSON output with detection details
4. Result images are also stored in the `outputs/` folder.

---

## Environment Variables

The `docker-compose.yml` file supports overrides using environment variables:

- `AI_BACKEND_PORT` → default: `8001`
- `UI_BACKEND_PORT` → default: `8002`
- `STREAMLIT_PORT` → default: `8003`
- `OUTPUT_DIR` → default: `./outputs`

You can set them in a `.env` file at the root.

---

## References

- [YOLOv5 – Ultralytics Implementation](https://github.com/ultralytics/yolov5)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Docker Compose](https://docs.docker.com/compose/)

