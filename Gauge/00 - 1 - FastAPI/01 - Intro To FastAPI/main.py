from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello, World!"}