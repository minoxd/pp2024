def student(stdscr, s_list, c_list, m_list):
    stdscr.clear()
    stdscr.refresh()
    y = y_choice(1)
    while True:
        curses_student(stdscr)
        try:
            select = int(ask_menu_choice(y))
        except ValueError:
            select = -1
        match select:
            case 0:
                return s_list, c_list, m_list
            case 1:
                s_list, m_list = add_student(stdscr, s_list, c_list, m_list)
            case 2:
                s_list, m_list = add_n_student(stdscr, s_list, c_list, m_list)
            case 3:
                s_list, m_list = del_student(stdscr, s_list, m_list)
            case 4:
                s_list, m_list = del_n_student(stdscr, s_list, m_list)
            case 5:
                s_list = del_all_elements(stdscr, s_list, 0)
                m_list = []
            case 6:
                s_list, c_list, m_list = view_update_student(stdscr, s_list, c_list, m_list)
            case 7:
                print_list_get_element(stdscr, s_list, 0, False)
            case 8:
                obj = Student()
                obj.print_list_gpa_desc(stdscr, s_list, c_list, m_list)
            case _:
                invalid_choice(stdscr, y)


def curses_course(stdscr):
    option = [
        "Exit",
        "Add a new course",
        "Delete a course",
        "View/Update an existing course",
        "List all courses"
    ]
    stdscr.clear()
    stdscr.addstr(1, 8, "STUDENT LIST")
    for i in range(5):
        stdscr.addstr(3 + i, 0, f"[{i}] {option[i]}")

    stdscr.addstr(13, 0, "Enter your choice: ")
    stdscr.refresh()