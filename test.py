import curses
from curses import wrapper
from curses.textpad import Textbox
error = []  # todo
warn = []


def menu_home(stdscr):
    option = [
        "Exit",
        "Students",
        "Courses",
        "Quick options"
    ]

    stdscr.addstr(1, 8, "STUDENT MARK PROGRAM")
    for i in range(4):
        stdscr.addstr(3 + i, 0, f"[{i}] {option[i]}")

    stdscr.addstr(15, 0, "Enter your choice: ")
    stdscr.refresh()
    win = curses.newwin(1, 30, 15, 19)
    box = Textbox(win)

    curses.curs_set(1)
    box.edit()
    curses.curs_set(0)
    text = box.gather()
    stdscr.addstr(16, 0, f"{str(type(text))}: {text}")
    stdscr.getch()


def main(stdscr):
    curses.use_default_colors()
    curses.curs_set(0)
    menu_home(stdscr)


wrapper(main)

