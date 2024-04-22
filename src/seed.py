'''seed.py'''

from sqlalchemy.orm import sessionmaker, Session
from models.base import Base
from models.pizza import PizzaModel
from models.comment import CommentModel
from data.pizza_data import pizzas_list, comments_list
from data.user_data import user_list
from config.environment import db_URI
from sqlalchemy import create_engine

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

# ! This seed file is a separate program that can be used to "seed" our database with some initial data.
try:
    print("Recreating database..")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("seeding our database..")
    # ! Seed pizzas
    db = SessionLocal()
    db.add_all(user_list)
    db.commit()

    db.add_all(pizzas_list)
    db.commit()

    db.add_all(comments_list)
    db.commit()

    db.close()
    # db = SessionLocal()
    # db.add_all(pizzas_db)
    # db.commit()
    # db.close()

    print("bye 👋")
except Exception as e:
    print(e)

