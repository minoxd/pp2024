import curses
from curses import wrapper
from curses.textpad import Textbox
error = []
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
    stdscr.addstr(8, 0, "Enter your choice: ")
    win = curses.newwin(1, 20, 8, 19)
    box = Textbox(win)
    stdscr.refresh()
    curses.curs_set(1)
    box.edit()
    curses.curs_set(0)
    text = box.gather()
    stdscr.addstr(10, 0, f"{str(type(int(text)))}: {text}")
    stdscr.getch()


def main(stdscr):
    curses.use_default_colors()
    curses.curs_set(0)
    menu_home(stdscr)


wrapper(main)

