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
            option = int(input("Enter your choice: "))
        except ValueError:
            option = -1
        match option:
            case 0:
                print("""
        THANK YOU FOR USING MY PROGRAMME!!""")
                return
            case 1:
                student(list_student)
            case 2:
                course(list_course)
            case 3:
                return
            case _:
                print("\tInvalid option!")


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
[6] View details of a student
[7] Update an existing student
[8] List all students
""")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            option = -1
        match option:
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
                list_student = del_all_student(list_student)
            case 6:
                view_a_student(list_student)
            case 7:
                list_student = update_student(list_student)
            case 8:
                list_all_students(list_student)
            case _:
                print("\tInvalid option!")


def add_student(list_student):
    list_student += [{}]
    list_student[-1] = {
        "id": len(list_student),
        "name": str(input("Enter student name: ")),
        "dob": get_dob()
    }
    return list_student


def get_dob():
    while True:
        try:
            print("Please enter the birthday in the following order: year, month, day.")
            dob = date(
                year=int(input("Year: ")),
                month=int(input("Month: ")),
                day=int(input("Day: "))
            )
            break
        except ValueError as ve:
            print(f"\n\tInvalid input: {ve}!")
    return dob


def add_n_student(list_student):
    while True:
        try:
            times = int(input("Enter number of new students ([0] to exit): "))
        except ValueError:
            times = -1
        if times == 0:
            return list_student
        if times < 0:
            print("\tInvalid input!")
        else:
            for i in range(times):
                print(f"\n\tEnter information for the {ordinal(i + 1)} student: ")
                list_student = add_student(list_student)
            break
    return list_student


def ordinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix


def del_student(list_student):
    num_students = len(list_student)
    if list_no_element(list_student, 0):
        return list_student
    student_selection = print_list_get_element(list_student, 0)
    index = student_selection - 1
    if student_selection == 0:
        return list_student
    print(f"Deleted {get_name(list_student, index)}.")
    del list_student[index]
    list_no_element(list_student, 0)
    # reassign id
    for i in range(num_students - student_selection):
        list_student[index + i]["id"] -= 1
    return list_student


def list_no_element(the_list, mode):
    num_element = len(the_list)
    cate = [
        "student in the class",
        "course available"
    ]
    if num_element < 1:
        print(f"There is no {cate[mode]}.")
        return True
    return False


def print_list_get_element(the_list, mode):
    num_element = len(the_list)
    cate = [
        "STUDENT LIST",
        "COURSE AVAILABLE"
    ]
    while True:
        print(f"""
        {cate[mode]}

[0] Exit""")
        for i in range(num_element):
            print(f"[{i + 1}] {get_name(the_list, i)}")
        print("")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            option = -1
        if 0 <= option <= num_element:
            return option
        else:
            print("\tInvalid option!")


def get_name(the_list, index):
    return the_list[index]["name"]


def del_n_student(list_student):
    while True:
        try:
            times = int(input("Enter number of students to be deleted ([0] to exit): "))
        except ValueError:
            times = -1
        if times == 0:
            return list_student
        if times < 0 or times > len(list_student):
            print("\tInvalid input!")
        else:
            for i in range(times):
                list_student = del_student(list_student)
            break
    return list_student


def del_all_student(list_student):
    key = "yesyesyes"
    while True:
        print(f"""
        WARNING: THIS PROCESS CANNOT BE UNDONE
        ARE YOU SURE YOU WANT TO DELETE ALL STUDENTS IN THE CLASS?

[0] Exit
[!] Type "{key}" to confirm the deletion
""")
        option = input("Enter your answer: ")
        if option == "0":
            return list_student
        if option == key:
            print("There is no student left.")
            return []
        print("\tInvalid input!")


def view_a_student(list_student):
    if list_no_element(list_student, 0):
        return
    student_selection = print_list_get_element(list_student, 0)
    index = student_selection - 1
    if student_selection == 0:
        return
    print(f"""
    Student:\t\t\t{get_name(list_student, index)}
    ID:\t\t\t\t\t{list_student[index]["id"]}
    DOB (YYYY-MM-DD):\t{list_student[index]["dob"]}""")
    return


def update_student(list_student):
    if list_no_element(list_student, 0):
        return list_student
    student_selection = print_list_get_element(list_student, 0)
    index = student_selection - 1
    if student_selection == 0:
        return list_student

    while True:
        print(f"""
        SELECTED STUDENT
    Student:\t\t\t{get_name(list_student, index)}
    ID:\t\t\t\t\t{list_student[index]["id"]}
    DOB (YYYY-MM-DD):\t{list_student[index]["dob"]}

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
                list_student[student_selection - 1]["name"] = str(input("Enter name: "))
            case 2:
                list_student[student_selection - 1]["dob"] = get_dob()
            case _:
                print("\tInvalid option!")


def list_all_students(list_student):
    num_student = len(list_student)
    if list_no_element(list_student, 0):
        return
    print(f"""
        STUDENT LIST

    Number of students: {num_student}
    Listing all students:""")
    for i in range(num_student):
        print(f"{get_name(list_student, i)}")
    return


def course(list_course):
    while True:
        print(f"""
        COURSE LIST

[0] Exit
[1] Add a new course
[3] Delete a course
[6] View details of a course
[7] Update an existing course
[8] List all courses
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
            case 3:
                list_course = del_course(list_course)
            case 6:
                view_a_course(list_course)
            case 7:
                list_course = update_course(list_course)
            case 8:
                list_all_courses(list_course)
            case _:
                print("\tInvalid option!")


def add_course(list_course):
    list_course += [{}]
    list_course[-1] = {
        "id": len(list_course),
        "name": str(input("Enter course name: ")),
        "mark": []
    }
    return list_course


def del_course(list_course):
    num_courses = len(list_course)
    if list_no_element(list_course, 1):
        return list_course
    course_selection = print_list_get_element(list_course, 1)
    index = course_selection - 1
    if course_selection == 0:
        return list_course
    print(f"Deleted {get_name(list_course, index)}.")
    del list_course[index]
    list_no_element(list_course, 1)
    # reassign id
    for i in range(num_courses - course_selection):
        list_course[index + i]["id"] -= 1
    return list_course


def view_a_course(list_course):  # TODO
    pass


def update_course(list_course):
    pass


def list_all_courses(list_course):
    pass


def main():
    # init
    students = []
    courses = []

    home(students, courses)


if __name__ == "__main__":
    main()
