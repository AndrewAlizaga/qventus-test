# Python base image
FROM python:3.12-slim

# Install Rust and system build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && curl https://sh.rustup.rs -sSf | sh -s -- -y \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set Cargo path so pip can find it
ENV PATH="/root/.cargo/bin:$PATH"

# Set PYTHON PATH
ENV PYTHONPATH=/app

WORKDIR /main

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY ./app ./app

# Expose port
EXPOSE 8000

# Run the Server
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000"]

