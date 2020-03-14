#!/usr/bin/python3.8
from math import floor
import curses
from typing import List
import os
import sys
dataSourcesDir = os.path.dirname(os.path.realpath(__file__)) + '/dataSources'
sys.path.append(dataSourcesDir)
from abstractmenusource import Dish, Nutrition, Menu
from stwnodatasource import StwnoDataSource

# column width in percent for each of the attributes of a Dish. Longer strings are cut
WIDTH_NAME = 60
WIDTH_NUTRITION_TYPE = 10
WIDTH_PRICE = 10
COLUMN_SEPARATOR = '|'
COLUMN_OFFSET_LEFT = 2

def dishToString(dish: Dish) -> str:
    # set menu name
    CC_NAME = floor(WIDTH_NAME / 100 * curses.COLS)
    line = dish['name'].ljust(CC_NAME)

    # set meal category
    CC_NUT_TYPE = floor(WIDTH_NUTRITION_TYPE / 100 * curses.COLS)
    line += dish['nutritionType'].symbol.center(CC_NUT_TYPE)

    # set price category
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
    try:
        menu = dataSource.getMenu()
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
    curses.wrapper(main)
