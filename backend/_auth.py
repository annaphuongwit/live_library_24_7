import os, datetime
from passlib.hash import bcrypt
import jwt
from sqlalchemy.orm import Session
from backend._models import User

JWT_SECRET = os.getenv("JWT_SECRET","dev-secret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM","HS256")
JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES","120"))

def hash_password(raw: str) -> str:
    return bcrypt.hash(raw)

def verify_password(raw: str, hashed: str) -> bool:
    return bcrypt.verify(raw, hashed)

def create_access_token(sub: str) -> str:
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=JWT_EXPIRE_MINUTES)
    payload = {"sub": sub, "exp": expire}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def authenticate(db: Session, email: str, password: str) -> User | None:
    user = db.query(User).filter(User.email == email).first()
    if user and verify_password(password, user.password_hash):
        return user
    return None
