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

class MealCategories():
    class MealCategory():
        def __init__(self, identifier: int, name: str):
            self.identifier = identifier
            self.name = name
        def __lt__(self, other):
            return self.identifier < other.identifier
    starter = MealCategory(1, 'STARTERS')
    mainDish = MealCategory(2, 'MAIN DISHES')
    sideDish = MealCategory(3, 'SIDE DISHES')
    dessert = MealCategory(4, 'DESSERTS')

class Dish(TypedDict):
    name: str
    category: MealCategories.MealCategory
    nutritionType: Nutrition.NutritionType
    price: float

class AbstractMenuSource(abc.ABC):
    @abc.abstractmethod
    def getMenu(self, params) -> List[Dish]:
        pass
        
