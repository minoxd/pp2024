import curses
import sys
import time
from curses import wrapper
from curses.textpad import Textbox

error = []  # todo
warn = []


def test_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Hello World!")
    stdscr.addstr(1, 0, "Hello World!", curses.A_BOLD)
    stdscr.addstr(2, 0, "Hello World!", curses.A_ITALIC)
    stdscr.refresh()
    curses.nl()
    stdscr.getch()



def main(stdscr):
    curses.use_default_colors()
    curses.curs_set(0)
    test_screen(stdscr)


try:
    wrapper(main)
except KeyboardInterrupt:
    print("\033[91m" + "\n\nForced to exit using keyboard!" + "\033[0m")
