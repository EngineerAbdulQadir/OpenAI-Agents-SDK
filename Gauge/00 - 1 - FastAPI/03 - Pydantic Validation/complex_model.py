from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import uuid4

app = FastAPI(
    title="DACA Chatbot API",
    description="A FastAPI-based API for a chatbot in the DACA tutorial series",
    version="0.1.0",
)


class Metadata(BaseModel):
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(tz=timezone.utc),
        description="UTC timestamp when the message was created"
    )
    session_id: str = Field(c
        default_factory=lambda: str(uuid4()),
        description="Unique session identifier"
    )

class Message(BaseModel):
    user_id: str = Field(..., description="Unique identifier for the user")
    text: str = Field(..., min_length=1, description="The user's message text")
    metadata: Metadata
    tags: list[str] | None = Field(None, description="Optional list of tags/classifiers")

class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata


@app.get("/")
async def root():
    """
    Root endpoint.
    """
    return {
        "message": "Welcome to the DACA Chatbot API! Visit /docs for the interactive API docs."
    }

@app.get("/users/{user_id}")
async def get_user(user_id: str, role: str | None = None):
    """
    Retrieve basic user info.
    - **user_id**: path parameter
    - **role**: optional query parameter (default “guest”)
    """
    return {
        "user_id": user_id,
        "role": role or "guest"
    }

@app.post("/chat/", response_model=Response)
async def chat(message: Message):
    """
    Chat endpoint.
    - Validates the incoming Message (including nested Metadata).
    - Returns a Response with its own Metadata.
    """
    if not message.text.strip():
        raise HTTPException(status_code=400, detail="Message text cannot be empty")

    reply_text = (
        f"Hello, {message.user_id}! You said: “{message.text}”. "
        "How can I assist you today?"
    )

    return Response(
        user_id=message.user_id,
        reply=reply_text,
        metadata=Metadata()
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("complex_model:app", host="0.0.0.0", port=8000, reload=True)