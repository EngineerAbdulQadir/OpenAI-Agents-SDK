from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import uvicorn

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None

fake_users: dict[int, User] = {}

@app.post("/users/", response_model=User)
async def create_user(user: User):
    """
    Create a new user.  
    - Validates payload against the `User` model.
    - Returns 422 if the payload doesn’t match types/requirements.
    """
    if user.id in fake_users:
        raise HTTPException(status_code=400, detail="User ID already exists")
    fake_users[user.id] = user
    return user

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    """
    Retrieve a user by ID.  
    - Returns 404 if the user is not found.
    """
    if user_id not in fake_users:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_users[user_id]

if __name__ == "__main__":
    uvicorn.run("basic_model:app", host="0.0.0.0", port=8000)