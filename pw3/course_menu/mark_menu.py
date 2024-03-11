from pw3.course_menu.add_mark import add_mark
from pw3.course_menu.add_n_mark import add_n_mark
from pw3.course_menu.del_all_mark import del_all_mark
from pw3.course_menu.del_mark import del_mark
from pw3.course_menu.del_n_mark import del_n_mark
from pw3.course_menu.print_mark import print_mark
from pw3.course_menu.update_mark import update_mark
from pw3.utils.list_no_element import list_no_element


def mark(s_list, c_list, c_index, m_list):
    while True:
        print()
        if list_no_element(s_list, 0):
            return m_list
        print_mark(s_list, c_list, c_index, m_list, 0)
        print("""
[0] Exit
[1] Add mark for a student
[2] Add mark for n student
[3] Delete mark for a student
[4] Delete marks for n student
[5] Delete all marks
[6] Update an existing mark
""")
        try:
            selection = int(input("Enter your choice: "))
        except ValueError:
            selection = -1
        match selection:
            case 0:
                return m_list
            case 1:
                m_list = add_mark(s_list, c_list, c_index, m_list)
            case 2:
                m_list = add_n_mark(s_list, c_list, c_index, m_list)
            case 3:
                m_list = del_mark(s_list, c_list, c_index, m_list)
            case 4:
                m_list = del_n_mark(s_list, c_list, c_index, m_list)
            case 5:
                m_list = del_all_mark(c_list, c_index, m_list)
            case 6:
                m_list = update_mark(s_list, c_list, c_index, m_list)
            case _:
                print("Invalid option!")


