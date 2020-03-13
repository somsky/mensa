#!/usr/bin/python3.8
from math import floor
import curses
from typing import List
import os
import sys
dataSourcesDir = os.path.dirname(os.path.realpath(__file__)) + '/dataSources'
sys.path.append(dataSourcesDir)
from abstractmenusource import Dish, Nutrition, MealCategories
from stwnodatasource import StwnoDataSource

# column width in percent for each of the attributes of a Dish. Longer strings are cut
WIDTH_NAME = 60
WIDTH_NUTRITION_TYPE = 10
WIDTH_PRICE = 10
COLUMN_SEPARATOR = '|'

def dishToString(dish: Dish) -> str:
    # set menu name
    CC_NAME = str(floor(WIDTH_NAME / 100 * curses.COLS))
    lineFormat = '{:' + CC_NAME + '.' + CC_NAME + '}' + '|'

    # set meal category
    CC_NUT_TYPE = str(floor(WIDTH_NUTRITION_TYPE / 100 * curses.COLS))
    lineFormat += '{:' + CC_NUT_TYPE + '.' + CC_NUT_TYPE + '}' + '|'

    # set price category
    CC_PRICE = str(floor(WIDTH_PRICE / 100 * curses.COLS))
    lineFormat += '{:' + CC_PRICE + '.' + CC_PRICE + '} €'

    return lineFormat.format(dish.get('name', 'n/a'),  dish.get('nutritionType').symbol, dish.get('price', 'n/a'))


def renderMenu(window, menu: List[Dish]):
    menu.dishes = sorted(menu.dishes, key=lambda dish: dish['category'])
    lastCat = None
    windowIndex = 1
    
    window.addstr(windowIndex, 1, menu.header)
    windowIndex += 1
    window.addstr(windowIndex, 1, menu.date)
    windowIndex += 1
    for menuIndex in range(0, len(menu.dishes)):
        # print heading for category
        currCat = menu.dishes[menuIndex].get('category')
        if currCat != lastCat:
            windowIndex += 1
            window.addstr(windowIndex, 1, '-- {} --'.format(currCat.name))
            windowIndex += 1
            lastCat = currCat
        window.addstr(windowIndex, 1, dishToString(menu.dishes[menuIndex]))
        windowIndex += 1


def main(stdscr):

    # curses stuff, set up the TUI
    stdscr.refresh()

    curses.start_color()
    curses.use_default_colors()

    win_height = curses.LINES
    win_width = curses.COLS

    menu_window = curses.newpad(win_height, win_width)
    menu_window.box()

    # todo: get the data source as a command line argument
    dataSource = StwnoDataSource()
    menu = dataSource.getMenu()
    renderMenu(menu_window, menu)

    menu_window.refresh(0,
                        0,
                        0,
                        0,
                        curses.LINES,
                        curses.COLS
                        )

    # Keep Window alive, read user input
    while True:
        key = stdscr.getkey()
        if key == 'q':
            sys.exit(1)
        menu_window.refresh(0,
                            0,
                            0,
                            0,
                            curses.LINES,
                            curses.COLS
                            )


if __name__ == '__main__':
    curses.wrapper(main)
