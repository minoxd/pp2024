from pw4.course_menu.add_course import add_course
from pw4.course_menu.add_mark import add_mark
from pw4.course_menu.print_mark import print_mark
from pw4.student_menu.add_n_student import add_n_student
from pw4.student_menu.add_student import add_student
from pw4.utils.print_list_get_element import print_list_get_element


def quick(s_list, c_list, m_list):
    while True:
        print("""
        QUICK OPTIONS

[0] Exit

    INPUT
[1] Add a new student
[2] Add multiple students
[3] Add a new course
[4] Add mark for a student

    LIST
[5] List all courses
[6] List all students
[7] View details of a course
    """)
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                return s_list, c_list, m_list
            case 1:
                s_list = add_student(s_list)
            case 2:
                s_list = add_n_student(s_list)
            case 3:
                c_list = add_course(c_list)
            case 4:
                c_select = print_list_get_element(c_list, 1, True)
                if c_select == 0:
                    return c_list
                c_index = c_select - 1

                m_list = add_mark(s_list, c_list, c_index, m_list)
            case 5:
                print_list_get_element(c_list, 1, False)
            case 6:
                print_list_get_element(s_list, 0, False)
            case 7:
                c_select = print_list_get_element(c_list, 1, True)
                if c_select == 0:
                    return c_list
                c_index = c_select - 1

                print_mark(s_list, c_list, c_index, m_list, 0)
            case _:
                print("Invalid option!")


