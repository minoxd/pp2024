from pw4.course_menu.mark_menu import mark
from pw4.course_menu.print_mark import print_mark
from pw4.utils.get_course_name_id import get_course_name_id
from pw4.utils.print_list_get_element import print_list_get_element


def view_update_course(s_list, c_list, m_list):
    c_select = print_list_get_element(c_list, 1, True)
    if c_select == 0:
        return c_list
    c_index = c_select - 1

    while True:
        print(f"""
        SELECTED COURSE
    Course:\t\t\t{get_course_name_id(c_list, c_index)}""")
        print_mark(s_list, c_list, c_index, m_list, 0)

        print("""
[0] Exit
[1] Change course name
[2] Update mark
""")
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                return c_list
            case 1:
                c_list[c_index].set_cname()
            case 2:
                m_list = mark(s_list, c_list, c_index, m_list)
            case _:
                print("Invalid option!")


