python
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: str
    email: str
    password: str
    name: str

class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    user_id: str