# ==============================================
# 🧠 Live Library Streamlit UI (Final Fixed)
# ==============================================

FROM python:3.11-slim

WORKDIR /app


RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev && rm -rf /var/lib/apt/lists/*


# ---- Copy project files ----
COPY . /app

# ---- Install Python packages ----
#RUN pip install --no-cache-dir --upgrade pip && \
RUN  pip install -r requirements.txt

# ---- Expose port ----
#EXPOSE 8000
EXPOSE 8051

# ---- Start Streamlit ----
#CMD ["streamlit", "run", "backend/homepage.py", "--server.port=8051", "--server.address=0.0.0.0"]
CMD ["streamlit", "run", "backend/app.py", "--server.port=8051", "--server.address=0.0.0.0"]


# CMD ["bash", "-c", "cd backend && streamlit run homepage.py --server.port=8000 --server.address=0.0.0.0"]
