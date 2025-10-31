# ==============================================
# 🐍 Backend Dockerfile (FastAPI + MySQL Client)
# ==============================================

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy backend code
COPY ./backend /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
