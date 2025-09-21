FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 libglib2.0-0\
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r requirements.txt
COPY app.py detector.py ./
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
