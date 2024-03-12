from pw4.course_menu.add_course import add_course
from pw4.course_menu.del_course import del_course
from pw4.course_menu.view_update_course import view_update_course
from pw4.utils.print_list_get_element import print_list_get_element


def course(s_list, c_list, m_list):
    while True:
        print(f"""
        COURSE LIST

[0] Exit
[1] Add a new course
[2] Delete a course
[3] View/Update an existing course
[4] List all courses
""")
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                return s_list, c_list, m_list
            case 1:
                c_list = add_course(c_list)
            case 2:
                c_list, m_list = del_course(c_list, m_list)
            case 3:
                c_list = view_update_course(s_list, c_list, m_list)
            case 4:
                print_list_get_element(c_list, 1, False)
            case _:
                print("Invalid option!")


