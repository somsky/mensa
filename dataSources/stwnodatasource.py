import abstractmenusource
from typing import List
from abstractmenusource import Nutrition, MealCategories, Dish, AbstractMenuSource, Menu
try:
    import pyfiglet
except:
    pass


class StwnoDataSource(AbstractMenuSource):
    def getMenu(self) -> List[Dish]:
        restaurantName = 'OTH MENSA'
        dishes = [{'name': 'Schweiners', 'category': MealCategories.mainDish, 'nutritionType': Nutrition.meat, 'price': 4.50},
                {'name': 'Knödel', 'category': MealCategories.sideDish,
                    'nutritionType': Nutrition.vegetarian, 'price': 1.00},
                {'name': 'Krautschupfnudeln', 'category': MealCategories.mainDish,
                    'nutritionType': Nutrition.vegetarian, 'price': 2.00},
                {'name': 'Pommes', 'category': MealCategories.sideDish, 'nutritionType': Nutrition.vegetarian, 'price': 1.50}]
        try:
            header = pyfiglet.figlet_format('OTH MENSA', font='slant')
        except:
            header = restaurantName
        return Menu(header, '15.03.2020', dishes)
