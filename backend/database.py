from dotenv import load_dotenv
import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# -------------------------------------------------
# 1️⃣ Load environment variables
# -------------------------------------------------
# Try local first, fallback to Docker path
env_path = Path(__file__).resolve().parent.parent / ".env"
if not env_path.exists():
    env_path = Path("/app/.env")
load_dotenv(dotenv_path=env_path)

# -------------------------------------------------
# 2️⃣ Fetch credentials from environment
# -------------------------------------------------
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "live_library_system")

# -------------------------------------------------
# 3️⃣ Build connection string
# -------------------------------------------------
from urllib.parse import quote_plus
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# -------------------------------------------------
# 4️⃣ Create engine and session
# -------------------------------------------------
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

