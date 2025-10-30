# 1️⃣ Base image
FROM python:3.11-slim

# 2️⃣ Set workdir
WORKDIR /app

# 3️⃣ Copy dependencies
COPY requirements.txt .

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy project files
COPY backend/ ./backend
COPY database/ ./database

# 6️⃣ Expose API port
EXPOSE 8000

# 7️⃣ Start FastAPI app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
