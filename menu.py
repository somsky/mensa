from typing import TypedDict
from enum import Enum

class MealType(Enum):
    VEGAN=1
    VEGETARIAN=2
    MEAT=2

class Menu(TypedDict):
    title: str
    name: str
    price: float
    mealType: MealType


