import abc
from typing import TypedDict, List
from enum import Enum

class NutritionType(Enum):
    UNKNOWN=1
    MEAT=2
    VEGETARIAN=3
    VEGAN=4

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
    nutritionType: NutritionType
    price: float

class AbstractMenuSource(abc.ABC):
    @abc.abstractmethod
    def getMenu(self, params) -> List[Dish]:
        pass
        
