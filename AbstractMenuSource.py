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
    def getMenu(self, address) -> List[Dish]:
        return [{'name': 'Schweiners', 'category': MealCategory.MAIN_DISH, 'nutritionType': NutritionType.MEAT, 'price': 4.50},
                {'name': 'Knödel', 'category': MealCategory.SIDE_DISH, 'nutritionType': NutritionType.VEGETARIAN, 'price': 1.00}]
        
