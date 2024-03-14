import curses
import time
from curses import wrapper


def main(stdscr):
    # curses.init_color(0, 0, 0, 0)
    # curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLUE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)

    pad = curses.newpad(100, 100)
    stdscr.refresh()
    for i in range(100):
        for j in range(26):
            char = chr(67+j)
            pad.addstr(char)
    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(0, i, 0, i, 25, 25 + i)
        time.sleep(.1)
    stdscr.getch()


wrapper(main)

