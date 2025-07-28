FROM python:3.10-slim

# install llama-cpp-python dependency
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only necessary files first
COPY setup.py README.md requirements.txt requirements.in ./
# Copy actual source code
COPY src/ src/
# Copy source code related to fastapi
COPY app/ app/
# Copy vector_db
COPY vector_db/ vector_db/

# Environment variable to trigger auto-download
ENV AUTO_DOWNLOAD_MODEL=true
ENV UPDATE_KNOWLEDGE_BASE=false

# Install dependencies
RUN pip install --upgrade pip && \
    pip install pip-tools && \
    pip install -r requirements.txt

# 修改 CMD
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]