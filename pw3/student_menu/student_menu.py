from pw3.student_menu.add_student import add_student
from pw3.student_menu.add_n_student import add_n_student
from pw3.student_menu.del_student import del_student
from pw3.student_menu.del_n_student import del_n_student
from pw3.utils.del_all_elements import del_all_elements
from pw3.student_menu.view_update_student import view_update_student
from pw3.utils.print_list_get_element import print_list_get_element


def student(s_list, m_list):
    while True:
        print(f"""
        STUDENT LIST 

[0] Exit
[1] Add a new student
[2] Add multiple students
[3] Delete a student
[4] Delete multiple students
[5] Delete all
[6] View/Update an existing student
[7] List all students
""")
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                return s_list, m_list
            case 1:
                s_list = add_student(s_list)
            case 2:
                s_list = add_n_student(s_list)
            case 3:
                s_list, m_list = del_student(s_list, m_list)
            case 4:
                s_list, m_list = del_n_student(s_list, m_list)
            case 5:
                s_list = del_all_elements(s_list, 0)
            case 6:
                s_list = view_update_student(s_list)
            case 7:
                print_list_get_element(s_list, 0, False)
            case _:
                print("Invalid option!")


