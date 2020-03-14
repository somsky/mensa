from typing import List
from abstractmenusource import Nutrition, Dish, AbstractMenuSource, Menu
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
        req = urllib.request.urlopen(apiUrl)
        res = json.loads(req.read())
        today = str(date.today())
        today = '2020-03-13'
        rawMenu = [menu for menu in res['days'] if today in menu['iso-date']]
        if len(rawMenu) == 0:
            raise Exception('Fetched menu contained no menu for today')
        rawMenu = rawMenu[0]
        menuDate = rawMenu['date']
        restaurantName = res['name']
        dishes = { 'main': [{'name': 'Schweiners', 'nutritionType': Nutrition.meat, 'pricing': 4.20}]}
        
        try:
            header = pyfiglet.figlet_format(restaurantName, font='slant')
        except:
            header = restaurantName
        return Menu(header, menuDate, dishes)
