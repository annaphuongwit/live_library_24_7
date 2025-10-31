from dotenv import load_dotenv
import os
from pathlib import Path
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# -------------------------------------------------
# 1️⃣ Load environment variables
# -------------------------------------------------
# This loads the .env file located in your project root
#load_dotenv(dotenv_path=".env")
env_path = Path(__file__).resolve().parent / ".env"
print(f"Loading .env from: {env_path}")  # Debug
load_dotenv(dotenv_path=env_path)
# -------------------------------------------------
# 2️⃣ Fetch credentials from environment
# -------------------------------------------------
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "living_library_manage_system")

# -------------------------------------------------
# 3️⃣ Create the DATABASE_URL safely
# -------------------------------------------------
#DATABASE_URL = f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# -------------------------------------------------
# 4️⃣ Initialize SQLAlchemy engine & session
# -------------------------------------------------
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# -------------------------------------------------
# 5️⃣ Test connection (optional, for debugging)
# -------------------------------------------------
if __name__ == "__main__":
    from sqlalchemy import text

    print("🔍 Debugging Database Connection...")
    print("Loaded DB_USER:", DB_USER)
    print("Loaded DB_PASSWORD:", DB_PASSWORD)
    print("Loaded DB_HOST:", DB_HOST)
    print("Loaded DB_NAME:", DB_NAME)
    print("Full DATABASE_URL:", DATABASE_URL)
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT DATABASE();"))
            db_name = result.scalar()
            print(f"✅ Connected successfully to database: {db_name}")
            print("📚 Listing tables:")
            tables = conn.execute(text("SHOW TABLES;")).fetchall()
            for t in tables:
                print("-", t[0])
    except Exception as e:
        print(f"❌ Connection failed: {e}")

# -------------------------------------------------
# 6️⃣ Dependency for FastAPI
# -------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

