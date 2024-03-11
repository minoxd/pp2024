from pw3.student_menu.add_student import add_student
from pw3.utils.ordinal import ordinal


def add_n_student(s_list):
    while True:
        try:
            times = int(input("""
[0] Exit
Enter number of new students: """))
        except ValueError:
            times = -1
        if times == 0:
            return s_list
        if times < 0:
            print("Invalid input!")
        else:
            for i in range(times):
                print(f"\nEnter information for the {ordinal(i + 1)} student: ")
                s_list = add_student(s_list)
            break
    return s_list


