# backend/Dockerfile

FROM python:3.11-slim

#WORKDIR /app/backend
WORKDIR /app

# Copy backend files only
#COPY ./backend /app/backend
#COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev && \
    pip install --no-cache-dir --upgrade pip && \
    pip install -r /app/requirements.txt && \
    rm -rf /var/lib/apt/lists/*

# Expose FastAPI port
EXPOSE 8001

# Run FastAPI backend
#CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8001"]
#WORKDIR /app  # ✅ switch working dir back to /app
CMD ["bash", "-c", "cd backend && uvicorn main:app --host 0.0.0.0 --port 8001"]