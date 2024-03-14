import curses
import sys
from curses import wrapper


def main(stdscr):
    curses.initscr()
    curses.newwin(1, curses.COLOR_WHITE, curses)
    stdscr.clear()
    stdscr.addstr(10, 10, "hello world", curses.A_BOLD)
    stdscr.addstr(15, 25, "at is great")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)


if __name__ == "__main__":
    try:
        main(stdscr=curses.initscr())
    except KeyboardInterrupt:
        print("\n\nForced to exit using keyboard!")
        sys.exit(0)

