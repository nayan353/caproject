""" pizza_data.py """

from models.pizza import PizzaModel
from models.comment import CommentModel
from models.user import UserModel

pizzas_list = [
    PizzaModel(name="Original", rating=4, in_stock=True, user_id=1),
    PizzaModel(name="Margerita", rating=4, in_stock=False, user_id=2),
    PizzaModel(name="BuffalowCHicken", rating=4, in_stock=True, user_id=3),
    PizzaModel(name="Veggie", rating=4, in_stock=False, user_id=4),
    PizzaModel(name="Alfredo", rating=4, in_stock=False, user_id=5),
    PizzaModel(name="White", rating=4, in_stock=False, user_id=6),
    PizzaModel(name="Vodka", rating=4, in_stock=False, user_id=7),
    PizzaModel(name="Penne", rating=4, in_stock=False, user_id=8),
    PizzaModel(name="ThinOriginal", rating=4, in_stock=False, user_id=9)
]

comments_list = [
    CommentModel(Non_veg="Yes",Peanut="Yes",Mushroom="Yes",Yeast="Yes", pizza_id=1),
    CommentModel(Non_veg="No",Peanut="No",Mushroom="Yes",Yeast="Yes", pizza_id=2),
    CommentModel(Non_veg="Yes",Peanut="No",Mushroom="Yes",Yeast="Yes", pizza_id=3),
    CommentModel(Non_veg="No",Peanut="Yes",Mushroom="Yes",Yeast="No", pizza_id=4),
    CommentModel(Non_veg="Yes",Peanut="No",Mushroom="No",Yeast="Yes", pizza_id=5),
    CommentModel(Non_veg="No",Peanut="No",Mushroom="Yes",Yeast="Yes", pizza_id=6),
    CommentModel(Non_veg="Yes",Peanut="No",Mushroom="No",Yeast="Yes", pizza_id=7),
    CommentModel(Non_veg="No",Peanut="No",Mushroom="No",Yeast="Yes", pizza_id=8),
    CommentModel(Non_veg="Yes",Peanut="Yes",Mushroom="Yes",Yeast="No", pizza_id=9)
]

