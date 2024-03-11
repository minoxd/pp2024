from pw3.utils.get_student_name_id import get_student_name_id
from pw3.utils.print_list_get_element import print_list_get_element


def view_update_student(s_list):
    s_select = print_list_get_element(s_list, 0, True)
    if s_select == 0:
        return s_list
    s_index = s_select - 1

    while True:
        print(f"""
        SELECTED STUDENT
    Student:\t\t\t{get_student_name_id(s_list, s_index)}
    DOB (YYYY-MM-DD):\t{s_list[s_index].get_sdob()}

[0] Exit
[1] Change name
[2] Change dob
""")
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                return s_list
            case 1:
                s_list[s_index].set_sname()
            case 2:
                s_list[s_index].set_sdob()
            case _:
                print("Invalid option!")


