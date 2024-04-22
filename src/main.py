""" main.py """




from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config.environment import db_URI
from controllers.pizzas import router as PizzasRouter
from controllers.users import router as UsersRouter
from database import get_db
import uvicorn

app = FastAPI()

app.include_router(PizzasRouter, prefix="/api")
app.include_router(UsersRouter, prefix="/api")

@app.get('/')
def home():
    """ Hello world function """
    return 'Welcome to Nayees Pizzeria!!'