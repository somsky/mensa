import abstractmenusource
from typing import List
from abstractmenusource import Nutrition, MealCategory, Dish, AbstractMenuSource 


class StwnoDataSource(AbstractMenuSource):
    def getMenu(self) -> List[Dish]:
        return [{'name': 'Schweiners', 'category': MealCategory.MAIN_DISH, 'nutritionType': Nutrition.meat, 'price': 4.50},
                {'name': 'Knödel', 'category': MealCategory.SIDE_DISH, 'nutritionType': Nutrition.vegetarian, 'price': 1.00},
                {'name': 'Krautschupfnudeln', 'category': MealCategory.MAIN_DISH, 'nutritionType': Nutrition.vegetarian, 'price': 2.00},
                {'name': 'Pommes', 'category': MealCategory.SIDE_DISH, 'nutritionType': Nutrition.vegetarian, 'price': 1.50}]
