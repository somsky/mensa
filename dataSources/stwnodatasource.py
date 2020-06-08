from typing import List
from abstractmenusource import Nutrition, Dish, AbstractMenuSource, Menu
import urllib.request
import json
from datetime import date

figlet = True

try:
    import pyfiglet
except:
    figlet = False

apiUrl = "https://app.mensaplan.de/api/11102/de.mensaplan.app.android.regensburg/reg7.json"


class StwnoDataSource(AbstractMenuSource):
    def getMenu(self) -> Menu:
        req = urllib.request.urlopen(apiUrl)
        res = json.loads(req.read())
        today = str(date.today())
        rawMenu = [menu for menu in res['days'] if today in menu['iso-date']]
        if len(rawMenu) == 0:
            raise Exception('Fetched menu contained no menu for today')
        rawMenu = rawMenu[0]
        menu = {category['name']: [{'name': meal['name'].replace('\xad', ''), 'nutritionType': Nutrition.meat, 'pricing': meal['pricing']
                                    ['for'][0] / 100} for meal in category['meals']] for category in rawMenu['categories']}
        menuDate = rawMenu['date']
        restaurantName = res['name']

        if figlet:
            header = pyfiglet.figlet_format(restaurantName, font='slant')
        else:
            header = restaurantName
        return Menu(header, menuDate, menu)
