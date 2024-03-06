# seems like there is no such thing called
# different constructor for different parent
from datetime import date


def home(list_student, list_course):
    while True:
        print("""
        STUDENT MARK PROGRAM

[0] Exit
[1] Students
[2] Courses
[3] Quick options
""")
        try:
            selection = int(input("Enter your choice: "))
        except ValueError:
            selection = -1
        match selection:
            case 0:
                print("""
        THANK YOU FOR USING MY PROGRAMME!!""")
                return
            case 1:
                student(list_student)
            case 2:
                pass
                course(list_course, list_student)
            case 3:
                pass
                # quick(list_course, list_student)
            case _:
                print("Invalid option!")


def student(list_student):
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
            selection = int(input("Enter your choice: "))
        except ValueError:
            selection = -1
        match selection:
            case 0:
                return
            case 1:
                list_student = add_student(list_student)
            case 2:
                list_student = add_n_student(list_student)
            case 3:
                list_student = del_student(list_student)
            case 4:
                list_student = del_n_student(list_student)
            case 5:
                list_student = del_all_elements(list_student, 0)
            case 6:
                list_student = view_update_student(list_student)
            case 7:
                list_all_elements(list_student, 0)
            case _:
                print("Invalid option!")


def add_student(list_student):
    list_student.append(StudentMark(
        set_student_id(),
        input("Enter student name: "),
        set_student_dob()
    ))
    return list_student


def set_student_id():
    while True:
        try:
            sid = input("Enter student id: ")
            list_sid_obj = StudentMark()
            if sid in list_sid_obj.get_sm_list_sid():
                raise ValueError
            break
        except ValueError:
            print(f"\nID existed, try another one!")
    return sid


def set_student_dob():
    while True:
        try:
            print("Enter student birthday: ")
            dob = date(
                year=int(input("\tYear: ")),
                month=int(input("\tMonth: ")),
                day=int(input("\tDay: "))
            )
            break
        except ValueError as ve:
            print(f"\nInvalid input: {ve}!")
    return dob


# def add_n_student(list_student):
#     while True:
#         try:
#             times = int(input("""
# [0] Exit
# Enter number of new students: """))
#         except ValueError:
#             times = -1
#         if times == 0:
#             return list_student
#         if times < 0:
#             print("Invalid input!")
#         else:
#             for i in range(times):
#                 print(f"\nEnter information for the {ordinal(i + 1)} student: ")
#                 list_student = add_student(list_student)
#             break
#     return list_student


# def ordinal(n: int):
#     if 11 <= (n % 100) <= 13:
#         suffix = 'th'
#     else:
#         suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
#     return str(n) + suffix


def del_student(list_student):
    student_selection = print_list_get_element(list_student, 0)
    if student_selection is False or student_selection == 0:
        return list_student
    student_index = student_selection - 1

    print(f"Deleted {get_student_name_id(list_student, student_index)}.")
    list_sid_obj = StudentMark()
    list_sid_obj.set_sm_list_sid(
        list_sid_obj.get_sm_list_sid().remove(
            list_student[student_index].get_sm_sid()
        )
    )

    del list_student[student_index]
    return list_student


def print_list_get_element(the_list, mode):
    num_element = len(the_list)
    label1 = [
        "student in the class",
        # "course available",
        # "mark"
    ]
    if num_element < 1:
        print(f"There is no {label1[mode]}.")
        return False
    label2 = [
        "STUDENT LIST",
        # "COURSE AVAILABLE"
    ]
    while True:
        print(f"""
        {label2[mode]}

[0] Exit""")
        for i in range(num_element):
            name_id = get_student_name_id(the_list, i)
            print(f"[{i + 1}] {name_id}")
        print()
        try:
            selection = int(input("Enter your choice: "))
        except ValueError:
            selection = -1
        if 0 <= selection <= num_element:
            return selection
        else:
            print("Invalid option!")


def get_student_name_id(the_list, index):
    the_name = the_list[index].get_sm_sname()
    the_id = the_list[index].get_sm_sid()
    return f"{the_name} (ID: {the_id})"


def del_n_student(list_student):
    while True:
        try:
            times = int(input("""
[0] Exit
Enter number of students to be deleted: """))
        except ValueError:
            times = -1
        if times == 0:
            return list_student
        if times < 0 or times > len(list_student):
            print("Invalid input!")
        else:
            for i in range(times):
                list_student = del_student(list_student)
            break
    return list_student


def del_all_elements(the_list, mode):
    key = "yesyesyes"
    label1 = [
        "STUDENTS IN THE CLASS",
        # "MARKS IN THE COURSE"
    ]
    label2 = [
        "student",
        # "mark"
    ]
    while True:
        print(f"""
        WARNING: THIS PROCESS CANNOT BE UNDONE
        ARE YOU SURE YOU WANT TO DELETE ALL {label1[mode]}?

[0] Exit
[!] Type "{key}" to confirm the deletion
""")
        option = input("Enter your answer: ")
        if option == "0":
            return the_list
        if option == key:
            print(f"There is no {label2[mode]} left.")
            list_sid_obj = StudentMark()
            list_sid_obj.set_sm_list_sid([])
            return []
        print("Invalid input!")


def view_update_student(list_student):
    student_selection = print_list_get_element(list_student, 0)
    if student_selection is False or student_selection == 0:
        return list_student
    student_index = student_selection - 1

    while True:
        print(f"""
        SELECTED STUDENT
    Student:\t\t\t{get_student_name_id(list_student, student_index)}
    DOB (YYYY-MM-DD):\t{list_student[student_index].get_sm_sdob()}

[0] Exit
[1] Change name
[2] Change dob
""")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            option = -1
        match option:
            case 0:
                return list_student
            case 1:
                list_student[student_index].set_sm_sname(
                    str(input("Enter name: "))
                )
            case 2:
                list_student[student_index].set_sm_sdob(
                    set_student_dob()
                )
            case _:
                print("Invalid option!")


def list_all_elements(the_list, mode):
    num_elements = len(the_list)
    label1 = [
        "student in the class",
        # "course available",
        # "mark"
    ]
    if num_elements < 1:
        print(f"There is no {label1[mode]}.")
        return

    label2 = [
        "STUDENT LIST",
        # "COURSE LIST"
    ]
    label3 = [
        "students",
        # "courses"
    ]
    print(f"""
        {label2[mode]}

    Number of {label3[mode]}: {num_elements}
    Listing all {label3[mode]}:""")
    for i in range(num_elements):
        print(f"{get_student_name_id(the_list, i)}")
    return


def course(list_course, list_student):
    while True:
        print(f"""
        COURSE LIST

[0] Exit
[1] Add a new course
[2] Delete a course
[3] View details of a course
[4] Update an existing course
[5] List all courses
""")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            option = -1
        match option:
            case 0:
                return
            case 1:
                list_course = add_course(list_course)
            case 2:
                pass  # list_course = del_course(list_course)
            case 3:
                pass  # view_a_course(list_course, list_student)
            case 4:
                pass  # list_course = update_course(list_course, list_student)
            case 5:
                pass  # list_all_elements(list_course, 1)
            case _:
                print("Invalid option!")
            
            
def add_course(list_course):
    list_course.append(StudentMark(
        set_student_id(),
        input("Enter student name: "),
        set_student_dob()
    ))
    return list_course


class Student:
    __list_sid = []

    def __init__(self, sid, sname, sdob):
        self.__sid = sid
        Student.__list_sid.append(sid)
        self.__sname = sname
        self.__sdob = sdob

    # getters
    def get_list_sid(self):
        return self.__list_sid

    def get_sid(self):
        return self.__sid

    def get_sname(self):
        return self.__sname

    def get_sdob(self):
        return self.__sdob

    # setters
    def set_list_sid(self, new_list_sid):
        self.__list_sid = new_list_sid

    def set_sname(self, new_sname):
        self.__sname = new_sname

    def set_sdob(self, new_sdob):
        self.__sdob = new_sdob


class Course:
    def __init__(self):
        self.__cname = None

    def get_name(self):
        return self.__cname

    def set_name(self, newname):
        self.__cname = newname


class StudentMark(Student, Course):
    def __init__(
            self,
            sid="default",
            sname="default",
            sdob=date(1, 1, 1)):
        Student.__init__(self, sid, sname, sdob)

    # getters
    def get_sm_list_sid(self):
        return Student.get_list_sid(self)

    def get_sm_sid(self):
        return Student.get_sid(self)

    def get_sm_sname(self):
        return Student.get_sname(self)

    def get_sm_sdob(self):
        return Student.get_sdob(self)

    # setters
    def set_sm_list_sid(self, new_sm_list_sid):
        Student.set_list_sid(self, new_sm_list_sid)

    def set_sm_sname(self, new_sm_sname):
        Student.set_sname(self, new_sm_sname)

    def set_sm_sdob(self, new_sm_sdob):
        Student.set_sdob(self, new_sm_sdob)


def main():
    # init
    list_student = []
    list_course = []

    home(list_student, list_course)


if __name__ == "__main__":
    main()
