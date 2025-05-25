from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, validator, ValidationError
from typing import List
import uvicorn

app = FastAPI()

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: List[Address]

    @validator("name")
    def name_must_be_at_least_two_chars(cls, v: str) -> str:
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v

fake_users: dict[int, UserWithAddress] = {}

@app.post("/users/", response_model=UserWithAddress)
async def create_user(user: UserWithAddress):
    """
    Create a user with nested addresses.
    Enforces: name must be ≥ 2 chars, email valid, addresses valid.
    """
    if user.id in fake_users:
        raise HTTPException(status_code=400, detail="User ID already exists")
    fake_users[user.id] = user
    return user

@app.get("/users/{user_id}", response_model=UserWithAddress)
async def read_user(user_id: int):
    """
    Retrieve a user by ID.
    Returns 404 if not found.
    """
    if user_id not in fake_users:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_users[user_id]

if __name__ == "__main__":
    uvicorn.run("custom_validators:app", host="0.0.0.0", port=8000)