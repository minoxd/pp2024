from pw3.student_menu.del_student import del_student
from pw3.utils.ordinal import ordinal


def del_n_student(s_list, m_list):
    while True:
        try:
            times = int(input("""
[0] Exit
Enter number of students to be deleted: """))
        except ValueError:
            times = -1
        if times == 0:
            return s_list
        if times < 0 or times > len(s_list):
            print("Invalid input!")
        else:
            for i in range(times):
                print(f"The {ordinal(i + 1)} student to be deleted: ")
                s_list = del_student(s_list, m_list)
            break
    return s_list, m_list


