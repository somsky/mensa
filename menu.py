#!/usr/bin/python3.8
import sys
import os
dataSourcesDir = os.path.dirname(os.path.realpath(__file__)) + '/dataSources'
sys.path.append(dataSourcesDir)
from stwnodatasource import StwnoDataSource
import curses

menuAddr = "https://app.mensaplan.de/api/11102/de.mensaplan.app.android.regensburg/reg7.json"


def main(stdscr):

    # curses stuff, set up the TUI
    stdscr.refresh()

    curses.start_color()
    curses.use_default_colors()

    win_height = curses.LINES
    win_width = curses.COLS

    menu_window = curses.newpad(win_height, win_width)
    menu_window.box() 
    menu_window.addstr('hello, I am a window')


    menu_window.refresh(0,
        0,
        0,
        0,
        curses.LINES,
        curses.COLS
    )


    # todo: get the data source as a command line argument
    dataSource = StwnoDataSource()

    menu = dataSource.getMenu()

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
