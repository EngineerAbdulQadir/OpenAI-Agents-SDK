from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str | None = Query(
        None,                            
        title="Query string",            
        description="Query string for searching items",
        min_length=3,
        max_length=50
    ),
    skip: int = Query(
        0,                               
        title="Items to skip",
        description="Number of items to skip (>= 0)",
        ge=0
    ),
    limit: int = Query(
        10,                             
        title="Items to return",
        description="Maximum number of items to return (<= 100)",
        le=100
    )
):
    """
    - **q**: optional search term (3–50 chars)  
    - **skip**: how many items to skip (>=0)  
    - **limit**: max items to return (<=100)  
    """
    return {"q": q, "skip": skip, "limit": limit}

if __name__ == "__main__":
    uvicorn.run("query_parameter:app", host="127.0.0.1", port=8000, reload=True)
