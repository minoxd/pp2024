from pw3.student_menu.student_menu import student
from pw3.course_menu.course_menu import course
from pw3.quick_menu.quick_menu import quick


def home(s_list, c_list, m_list):
    while True:
        print("""
        STUDENT MARK PROGRAM

[0] Exit
[1] Students
[2] Courses
[3] Quick options
""")
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                print("""
        THANK YOU FOR USING MY PROGRAMME!!""")
                return s_list, c_list, m_list
            case 1:
                s_list, m_list = student(s_list, m_list)
            case 2:
                s_list, c_list, m_list = course(s_list, c_list, m_list)
            case 3:
                s_list, c_list, m_list = quick(s_list, c_list, m_list)
            case _:
                print("Invalid option!")


