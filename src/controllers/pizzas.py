'''controllers/pizzas.py'''

from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from models.pizza import PizzaModel
from models.user import UserModel
from serializers.pizza import PizzaSchema, PizzaCreate as PizzaCreateSchema
from typing import List
from database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/pizzas", response_model=List[PizzaSchema])
def get_pizzas(db: Session = Depends(get_db)):
    pizzas = db.query(PizzaModel).all()  
    return pizzas


@router.get("/pizzas/{pizza_id}", response_model=PizzaSchema)
def get_single_pizza(pizza_id: int, db: Session = Depends(get_db)):
    pizza = db.query(PizzaModel).filter(PizzaModel.id == pizza_id).first()
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return pizza


@router.post("/pizzas", response_model=PizzaSchema)
def create_pizza(pizza: PizzaCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    new_pizza = PizzaModel(**pizza.dict(), user_id=current_user.id)
    db.add(new_pizza)
    db.commit()
    db.refresh(new_pizza)
    return new_pizza


@router.put("/pizzas/{pizza_id}", response_model=PizzaSchema)
def update_pizza(pizza_id: int, pizza: PizzaCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # find the pizza to update
    db_pizza = db.query(PizzaModel).filter(PizzaModel.id == pizza_id).first()
    if not db_pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")

    # update the pizza
    pizza_data = pizza.dict(exclude_unset=True)
    for key, value in pizza_data.items():
        setattr(db_pizza, key, value)

    db.commit()
    db.refresh(db_pizza)
    return db_pizza


@router.delete("/pizzas/{pizza_id}")
def delete_pizza(pizza_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # find the pizza to delete
    db_pizza = db.query(PizzaModel).filter(PizzaModel.id == pizza_id).first()
    if not db_pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")

    db.delete(db_pizza)
    db.commit()
    return {"message": f"Pizza {pizza_id} deleted successfully"}

# @router.put("/pizzas/{pizza_id}")
# def order_pizza(pizza_id: int, db: Session = Depends(get_db)):
#     db_pizza = db.query(PizzaModel).filter(PizzaModel.rating == pizza_id.first()
#     db_test = PizzaModel.rating - 1
#     db.commit()
#     return {f"rating is {db_test}"}


    


