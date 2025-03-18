# Dockerfile
FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libssl-dev \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    git \
    netcat \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip==23.0.1 && \
    pip install --no-cache-dir pillow==9.0.1 && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir git+https://github.com/fananimi/pyzk.git

COPY ./src /app/src

ENV PYTHONPATH=/app/src

ENTRYPOINT ["/app/src/entrypoint.sh"]

