'''models/comment.py'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class CommentModel(BaseModel):

  __tablename__ = "comments"

  id = Column(Integer, primary_key=True, index=True)
  Non_veg = Column(String, nullable=False)
  Peanut = Column(String, nullable=False)
  Mushroom = Column(String, nullable=False)
  Yeast = Column(String, nullable=False)
  

  # ForeignKey points to the primary key (id) of the pizzas table
  pizza_id = Column(Integer, ForeignKey('pizzas.id'), nullable=False)
  pizza = relationship("PizzaModel", back_populates="comments")