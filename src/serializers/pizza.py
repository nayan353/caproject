'''serializers/pizza.py'''

from pydantic import BaseModel
from typing import Optional, List
from .comment import CommentSchema
from .user import UserSchema

class PizzaSchema(BaseModel):
  id: int
  name: str
  in_stock: bool
  rating: int
  user: UserSchema
  
  comments: List[CommentSchema] = []

  class Config:
    orm_mode = True

class PizzaCreate(BaseModel): 
    name: str
    in_stock: bool
    rating: int