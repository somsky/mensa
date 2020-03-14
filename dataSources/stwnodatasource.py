import abstractmenusource
from typing import List
from abstractmenusource import Nutrition, MealCategories, Dish, AbstractMenuSource, Menu
import urllib.request
import json
from datetime import date

try:
    import pyfiglet
except:
    pass

apiUrl = "https://app.mensaplan.de/api/11102/de.mensaplan.app.android.regensburg/reg7.json"

class StwnoDataSource(AbstractMenuSource):
    def getMenu(self) -> List[Dish]:
        #try:
        req = urllib.request.urlopen(apiUrl)
        res = json.loads(req.read())
        today = str(date.today())
        # print (res['days'])
        rawMenu = [menu for menu in res['days'] if today in menu['iso-date']]
        rawMenu = rawMenu[0]
        menuDate = rawMenu['date']
        restaurantName = res['name']

        dishes = [{'name': 'Schweiners', 'category': MealCategories.mainDish, 'nutritionType': Nutrition.meat, 'price': 4.50},
                {'name': 'Knödel', 'category': MealCategories.sideDish,
                    'nutritionType': Nutrition.vegetarian, 'price': 1.00},
                {'name': 'Krautschupfnudeln', 'category': MealCategories.mainDish,
                    'nutritionType': Nutrition.vegetarian, 'price': 2.00},
                {'name': 'Pommes', 'category': MealCategories.sideDish, 'nutritionType': Nutrition.vegetarian, 'price': 1.50}]
        try:
            header = pyfiglet.figlet_format(restaurantName, font='slant')
        except:
            header = restaurantName
        return Menu(header, '15.03.2020', dishes)
