import abstractmenusource
from typing import List
from abstractmenusource import Nutrition, MealCategories, Dish, AbstractMenuSource 


class StwnoDataSource(AbstractMenuSource):
    def getMenu(self) -> List[Dish]:
        return [{'name': 'Schweiners', 'category': MealCategories.mainDish, 'nutritionType': Nutrition.meat, 'price': 4.50},
                {'name': 'Knödel', 'category': MealCategories.sideDish, 'nutritionType': Nutrition.vegetarian, 'price': 1.00},
                {'name': 'Krautschupfnudeln', 'category':MealCategories.mainDish, 'nutritionType': Nutrition.vegetarian, 'price': 2.00},
                {'name': 'Pommes', 'category': MealCategories.sideDish, 'nutritionType': Nutrition.vegetarian, 'price': 1.50}]
