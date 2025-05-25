from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(
        ..., 
        title="Item ID", 
        ge=1, 
        description="Identifier of the item to update (must be ≥1)"
    ),
    q: str | None = Query(
        None, 
        min_length=3, 
        title="Query string", 
        description="Optional search or filter string (3+ chars)"
    ),
    item: Item | None = Body(
        None, 
        description="Optional JSON body with item details"
    )
):
    """
    Update an item:

    - **item_id** in the URL path (integer ≥1).  
    - Optional **q** in the query string (min length 3).  
    - Optional **item** in the JSON body matching the `Item` model.  
    """
    result: dict = {"item_id": item_id}
    if q:
        result["q"] = q
    if item:
        result["item"] = item.model_dump()
    return result

if __name__ == "__main__":
    uvicorn.run("body_parameter:app", host="127.0.0.1", port=8000, reload=True)