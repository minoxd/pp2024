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

            for i in range(999):
                pad.addstr(" ")

            for i in range(50):
                stdscr.clear()
                stdscr.refresh()
                pad.refresh(0, 0, 0, 0, 0 + i, 0 + i)
                time.sleep(.0001)
            stdscr.getch()
            break
        except curses.error:
            stdscr.clear()
            stdscr.refresh()
            curses.init_pair(1, curses.COLOR_RED, -1)
            stdscr.addstr("Please make your window larger!", curses.color_pair(1))
            stdscr.getch()


def main(stdscr):
    curses.use_default_colors()
    curses.curs_set(0)
    test_screen(stdscr)


try:
    wrapper(main)
except KeyboardInterrupt:
    print("\033[91m" + "\n\nForced to exit using keyboard!" + "\033[0m")
