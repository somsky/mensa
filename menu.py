#!/usr/bin/python3.8
from math import floor
import curses
from typing import List
import os
import sys
dataSourcesDir = os.path.dirname(os.path.realpath(__file__)) + '/dataSources'
sys.path.append(dataSourcesDir)
# pylint: disable=import-error
from abstractmenusource import Dish, Nutrition, Menu
from stwnodatasource import StwnoDataSource
import argparse
import importlib
import inspect

# column width in percent for each of the attributes of a Dish. Longer strings are cut
WIDTH_NAME = 60
WIDTH_NUTRITION_TYPE = 10
WIDTH_PRICE = 10
COLUMN_SEPARATOR = '|'
COLUMN_OFFSET_LEFT = 2

def dishToString(dish: Dish) -> str:
    # set menu name
    # pylint: disable=no-member
    CC_NAME = floor(WIDTH_NAME / 100 * curses.COLS)
    line = dish['name'].ljust(CC_NAME)

    # set meal category
    # pylint: disable=no-member
    CC_NUT_TYPE = floor(WIDTH_NUTRITION_TYPE / 100 * curses.COLS)
    line += dish['nutritionType'].symbol.center(CC_NUT_TYPE)

    # set price category
    # pylint: disable=no-member
    CC_PRICE = floor(WIDTH_PRICE / 100 * curses.COLS)
    line += '{:.2f}€'.format(dish['pricing']).center(CC_PRICE)
    return line


def renderMenu(window, menu: Menu):
    windowIndex = 1
    # print header, support multiline headers
    headerLines = menu.header.split('\n')
    for line in headerLines:
        window.addstr(windowIndex, COLUMN_OFFSET_LEFT, line)
        windowIndex += 1

    window.addstr(windowIndex, COLUMN_OFFSET_LEFT, menu.date)
    windowIndex += 1

    for mealCategory, dishes in menu.dishes.items():
        windowIndex += 1
        window.addstr(windowIndex, COLUMN_OFFSET_LEFT, '-- {} --'.format(mealCategory))
        windowIndex += 1
        for dish in dishes:
            window.addstr(windowIndex, COLUMN_OFFSET_LEFT, dishToString(dish))
        windowIndex += 1


def renderError(window, e):
    window.addstr(1, COLUMN_OFFSET_LEFT, str(e))

def main(dataSource, datasource_args):
    stdscr = curses.initscr()
    stdscr.refresh()
    curses.start_color()
    curses.use_default_colors()

    # pylint: disable=no-member
    win_height = curses.LINES
    # pylint: disable=no-member
    win_width = curses.COLS

    menu_window = curses.newpad(win_height, win_width)
    menu_window.box()

    try:
        menu = dataSource.getMenu(datasource_args) if datasource_args else dataSource.getMenu()
        renderMenu(menu_window, menu)
    except Exception as e:
        renderError(menu_window, e)

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
    parser = argparse.ArgumentParser()
    parser.add_argument('datasource', help='The name of the datasource you want to fetch todays menu from')
    parser.add_argument('-da', '--datasource_arg', help='Optional argument to send to the specified datasource')
    args = parser.parse_args()
    try:
        dataSourceModule = importlib.import_module(args.datasource)
    except ModuleNotFoundError:
        print('[ERR] Datasource "{}" not found'.format(args.datasource))
        sys.exit(-1)
    except Exception as e:
        print(e)
        sys.exit(-1)
    dataSourceClassNames = [m[0] for m in inspect.getmembers(dataSourceModule, inspect.isclass) if m[1].__module__ == args.datasource]
    dataSourceClasses = [getattr(dataSourceModule, dataSourceClassName) for dataSourceClassName in dataSourceClassNames]
    if len(dataSourceClasses) == 0:
        print('The specified datasource module contains serveral classes implementing the datasource interface')
        sys.exit(-1)
    elif len(dataSourceClasses) > 1:
        print('The specified datasource module contains no classes implementing the datasource interface')
    main(dataSourceClasses[0](), args.datasource_arg)
