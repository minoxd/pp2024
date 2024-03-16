import curses
import sys
import time
from curses import wrapper
from curses.textpad import Textbox

error = []  # todo
warn = []


def test_screen(stdscr):
    stdscr.addstr(14, 0, "Used student ids:          ", curses.color_pair(2))
    for i in range(len(self.__list_sid)):
        if i < 10:
            stdscr.addstr(15 + i, 0, self.__list_sid[i])
        else:
            stdscr.addstr(15 + i - 10, 25, self.__list_sid[i])
    stdscr.refresh()
    stdscr.getch()


def main(stdscr):
    curses.use_default_colors()
    curses.curs_set(0)
    test_screen(stdscr)


try:
    wrapper(main)
except KeyboardInterrupt:
    print("\033[91m" + "\n\nForced to exit using keyboard!" + "\033[0m")
