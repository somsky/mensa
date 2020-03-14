import abc from typing import TypedDict, List
from enum import Enum
from datetime import date
from typing import Dict

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


class Dish(TypedDict):
    name: str
    nutritionType: Nutrition.NutritionType
    pricing: float


class Menu():
    def __init__(self, header: str, date: str, dishes: List[Dish]):
        self.header = header
        self.date = date
        self.dishes = dishes
    dishes: Dict[str, List[Dish]]
    header: str
    date: date


class AbstractMenuSource(abc.ABC):
    @abc.abstractmethod
    def getMenu(self, params) -> Menu:
        pass
