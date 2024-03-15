import curses
import sys
import time
from curses import wrapper
from curses.textpad import Textbox
error = []  # todo
warn = []


def test_screen(stdscr):

    while True:
        try:
            pad = curses.newpad(20, 50)
            stdscr.refresh()

            for i in range(111):
                pad.addstr("abcdefgh ")

            while True:

                stdscr.clear()
                stdscr.refresh()
                pad.refresh(0, i, 0, 0, 20, 50)
                time.sleep(.1)
            stdscr.getch()
            break
        except curses.error:
            stdscr.clear()
            stdscr.refresh()
            curses.init_pair(1, curses.COLOR_RED, -1)
            stdscr.addstr("Error", curses.color_pair(1))
            stdscr.getch()


def main(stdscr):
    curses.use_default_colors()
    curses.curs_set(0)
    test_screen(stdscr)


try:
    wrapper(main)
except KeyboardInterrupt:
    print("\033[91m" + "\n\nForced to exit using keyboard!" + "\033[0m")
