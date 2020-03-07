import abstractmenusource
from typing import List
from abstractmenusource import NutritionType, MealCategory, Dish, AbstractMenuSource 


class StwnoDataSource(AbstractMenuSource):
    def getMenu(self) -> List[Dish]:
        return [{'name': 'Schweiners', 'category': MealCategory.MAIN_DISH, 'nutritionType': NutritionType.MEAT, 'price': 4.50},
                {'name': 'Knödel', 'category': MealCategory.SIDE_DISH, 'nutritionType': NutritionType.VEGETARIAN, 'price': 1.00}]
