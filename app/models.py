from typing import Optional, List
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    price: float = Field(..., gt=0)

class ItemResponse(ItemCreate):
    id: int

class User(BaseModel):
    id: int
    username: str
    is_active: bool = True
