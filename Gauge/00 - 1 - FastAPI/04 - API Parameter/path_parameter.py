from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        ...,                          
        title="The ID of the item",   
        description="A unique identifier for the item",
        ge=1,                         # >= 1
        le=1000                       # <= 1000
    )
):
    return {"item_id": item_id}

if __name__ == "__main__":
    uvicorn.run("path_parameter:app",  host="127.0.0.1",  port=8000, reload=True)