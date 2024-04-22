'''serializers/comment.py'''

from pydantic import BaseModel

class CommentSchema(BaseModel):
  id: int
  Non_veg: str
  Peanut: str
  Mushroom: str
  Yeast: str

  class Config:
    orm_mode = True
