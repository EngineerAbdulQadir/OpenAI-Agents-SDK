from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
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
    addresses: list[Address]   

fake_users: dict[int, UserWithAddress] = {}

@app.post("/users/", response_model=UserWithAddress)
async def create_user(user: UserWithAddress):
    """
    Create a new user with one or more addresses.
    """
    if user.id in fake_users:
        raise HTTPException(status_code=400, detail="User ID already exists")
    fake_users[user.id] = user
    return user

@app.get("/users/{user_id}", response_model=UserWithAddress)
async def read_user(user_id: int):
    """
    Retrieve a user and their addresses by ID.
    """
    if user_id not in fake_users:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_users[user_id]

if __name__ == "__main__":
    uvicorn.run("nested_model:app", host="0.0.0.0", port=8000)