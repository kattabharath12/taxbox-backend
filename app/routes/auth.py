
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(user: User):
    return {"message": f"User {user.email} registered"}

@router.post("/login")
def login(user: User):
    return {"token": "mock-jwt-token"}
