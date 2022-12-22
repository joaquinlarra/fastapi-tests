from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends, Header, status
from .models import ItemCreate, ItemResponse, User

app = FastAPI(title="FastAPI Testing Reference App")

# In-memory storage for demonstration
ITEMS_DB = []
USERS_DB = {
    "admin": User(id=1, username="admin", is_active=True),
    "user": User(id=2, username="user", is_active=True)
}

def get_current_user(authorization: Optional[str] = Header(None)) -> User:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid authentication token"
        )
    token = authorization.split(" ")[1]
    if token in USERS_DB:
        return USERS_DB[token]
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items", response_model=List[ItemResponse])
def get_items():
    return ITEMS_DB

@app.post("/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, user: User = Depends(get_current_user)):
    item_id = len(ITEMS_DB) + 1
    new_item = ItemResponse(id=item_id, **item.dict())
    ITEMS_DB.append(new_item)
    return new_item

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    for item in ITEMS_DB:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
