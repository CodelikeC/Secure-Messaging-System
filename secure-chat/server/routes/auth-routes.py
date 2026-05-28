from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from argon2 import PasswordHasher

from database import get_connection
from auth import create_token

router = APIRouter(prefix="/auth")

ph = PasswordHasher()

class RegisterRequest(BaseModel):
    username: str
    password: str
    public_key: str

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
async def register(data: RegisterRequest):

    conn = get_connection()
    cursor = conn.cursor()

    existing = cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (data.username,)
    ).fetchone()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    password_hash = ph.hash(data.password)

    cursor.execute("""
    INSERT INTO users (
        username,
        password_hash,
        public_key
    )
    VALUES (?, ?, ?)
    """, (
        data.username,
        password_hash,
        data.public_key
    ))

    conn.commit()
    conn.close()

    return {
        "message": "User registered successfully"
    }

@router.post("/login")
async def login(data: LoginRequest):

    conn = get_connection()
    cursor = conn.cursor()

    user = cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (data.username,)
    ).fetchone()

    conn.close()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    try:
        ph.verify(
            user["password_hash"],
            data.password
        )

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_token(data.username)

    return {
        "token": token
    }

@router.get("/public-key/{username}")
async def get_public_key(username: str):

    conn = get_connection()
    cursor = conn.cursor()

    user = cursor.execute(
        "SELECT public_key FROM users WHERE username=?",
        (username,)
    ).fetchone()

    conn.close()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "username": username,
        "public_key": user["public_key"]
    }