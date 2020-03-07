import abc
from typing import TypedDict, List
from enum import Enum

class NutritionType(Enum):
    MEAT=1
    VEGETARIAN=2
    VEGAN=3

class MealCategory(Enum):
    STARTER=1
    MAIN_DISH=2
    SIDE_DISH=3
    DESSERT=4

class Dish(TypedDict):
    name: str
    category: MealCategory
    nutritionType: NutritionType
    price: float

class AbstractMenuSource(abc.ABC):
    @abc.abstractmethod
    def getMenu(self, params) -> List[Dish]:
        pass
        
