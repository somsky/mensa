import abc
from typing import TypedDict, List
from enum import Enum

class Nutrition():
    class NutritionType():
        def __init__(self, name, symbol):
            self.name = name
            self.symbol = symbol
        def __eq__(self, other):
            return self.name == other.name
    unknown = NutritionType('unknown', 'n/a')
    meat = NutritionType('meat', 'meaty')
    vegetarian = NutritionType('vegetarian', 'veggy')
    vegan = NutritionType('vegan', 'vega')

class MealCategory(Enum):
    STARTER=1
    MAIN_DISH=2
    SIDE_DISH=3
    DESSERT=4
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

class Dish(TypedDict):
    name: str
    category: MealCategory
    nutritionType: Nutrition
    price: float

class AbstractMenuSource(abc.ABC):
    @abc.abstractmethod
    def getMenu(self, params) -> List[Dish]:
        pass
        
