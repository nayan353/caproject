'''models/pizza.py'''

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .comment import CommentModel
from .user import UserModel

class PizzaModel(BaseModel):

    
    #Postgresql
    __tablename__ = "pizzas"

    id = Column(Integer, primary_key=True, index=True)

    # ! Specific columns for our Pizza Table.
    name = Column(String, unique=True)
    in_stock = Column(Boolean)
    rating = Column(Integer)

    # Foreign key for User
    user_id = Column(Integer, ForeignKey('users.id'))

    # Many (PizzaModel) to One (UserModel) relationship
    user = relationship('UserModel', back_populates='pizzas')

    comments = relationship("CommentModel", back_populates="pizza")