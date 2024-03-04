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
                course(list_course, list_student)
            case 3:
                quick(list_course, list_student)
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
                list_student = del_all_elements(list_student, 0)
            case 6:
                view_a_student(list_student)
            case 7:
                list_student = update_student(list_student)
            case 8:
                list_all_elements(list_student, 0)
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
    if student_selection == 0:
        return list_student
    index = student_selection - 1
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
        "course available",
        "mark"
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
        print()
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            option = -1
        if 0 <= option <= num_element:
            return option
        else:
            print("\tInvalid option!")


def get_name(the_list, index):
    return f"{the_list[index]["name"]} (ID: {the_list[index]["id"]})"


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


def del_all_elements(the_list, mode):
    key = "yesyesyes"
    label1 = [
        "STUDENTS IN THE CLASS",
        "MARKS IN THE COURSE"
    ]
    label2 = [
        "student",
        "mark"
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
            return []
        print("\tInvalid input!")


def view_a_student(list_student):
    if list_no_element(list_student, 0):
        return
    student_selection = print_list_get_element(list_student, 0)
    if student_selection == 0:
        return
    index = student_selection - 1
    print(f"""
    Student:\t\t\t{get_name(list_student, index)}
    ID:\t\t\t\t\t{list_student[index]["id"]}
    DOB (YYYY-MM-DD):\t{list_student[index]["dob"]}""")
    return


def update_student(list_student):
    if list_no_element(list_student, 0):
        return list_student
    student_selection = print_list_get_element(list_student, 0)
    if student_selection == 0:
        return list_student
    index = student_selection - 1
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
                list_student[index]["name"] = str(input("Enter name: "))
            case 2:
                list_student[index]["dob"] = get_dob()
            case _:
                print("\tInvalid option!")


def list_all_elements(the_list, mode):
    num_elements = len(the_list)
    if list_no_element(the_list, mode):
        return
    label1 = [
        "STUDENT LIST",
        "COURSE LIST"
    ]
    label2 = [
        "students",
        "courses"
    ]
    print(f"""
        {label1[mode]}

    Number of {label2[mode]}: {num_elements}
    Listing all {label2[mode]}:""")
    for i in range(num_elements):
        print(f"{get_name(the_list, i)}")
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
                list_course = del_course(list_course)
            case 3:
                view_a_course(list_course, list_student)
            case 4:
                list_course = update_course(list_course, list_student)
            case 5:
                list_all_elements(list_course, 1)
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
    if course_selection == 0:
        return list_course
    index = course_selection - 1
    print(f"Deleted {get_name(list_course, index)}.")
    del list_course[index]
    list_no_element(list_course, 1)
    # reassign id
    for i in range(num_courses - course_selection):
        list_course[index + i]["id"] -= 1
    return list_course


def view_a_course(list_course, list_student):
    if list_no_element(list_course, 1):
        return
    course_selection = print_list_get_element(list_course, 1)
    if course_selection == 0:
        return
    index = course_selection - 1
    print(f"""
        SELECTED COURSE
    Course:\t\t{get_name(list_course, index)}
    ID:\t\t\t{list_course[index]["id"]}
    Mark status: """, end="")
    print_mark(list_course, index, list_student)
    return


def update_course(list_course, list_student):
    if list_no_element(list_course, 1):
        return list_course
    course_selection = print_list_get_element(list_course, 1)
    if course_selection == 0:
        return list_course
    index = course_selection - 1

    while True:
        print(f"""
        SELECTED COURSE
    Course:\t\t{get_name(list_course, index)}
    ID:\t\t\t{list_course[index]["id"]}
    Mark status: """, end="")
        print_mark(list_course, index, list_student)

        print("""
[0] Exit
[1] Change course name
[2] Update mark
""")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            option = -1
        match option:
            case 0:
                return list_course
            case 1:
                list_course[index]["name"] = str(input("Enter name: "))
            case 2:
                list_course[index]["mark"] = mark(list_course, index, list_student)
            case _:
                print("\tInvalid option!")


def print_mark(list_course, course_index, list_student):
    num_student = len(list_student)
    list_mark = list_course[course_index]["mark"]
    if not list_no_element(list_mark, 2):
        print(f"Marked {len(list_mark)}/{num_student} students.\n")
        for i in range(num_student):
            lookup_result = mark_lookup(list_course, course_index, i)
            if lookup_result != "n/a":
                lookup_result = lookup_result[0]
            print(f"{get_name(list_student, i)}: {lookup_result}")


def mark_lookup(list_course, course_index, student_index):
    sid = student_index + 1
    list_mark = list_course[course_index]["mark"]
    for i in list_mark:
        if i["student_id"] == sid:
            return [i["mark"], list_mark.index(i)]
    return "n/a"


def mark(list_course, course_index, list_student):
    while True:
        print("""
        Mark status: """, end="")
        print_mark(list_course, course_index, list_student)
        print("""
[0] Exit
[1] Add mark for a student
[2] Add mark for n student
[3] Delete mark for a student
[4] Delete marks for n student
[5] Delete all marks
[6] Update an existing mark
""")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            option = -1
        match option:
            case 0:
                return list_course[course_index]["mark"]
            case 1:
                list_course[course_index]["mark"] = add_mark(list_course, course_index, list_student)
            case 2:
                list_course[course_index]["mark"] = add_n_mark(list_course, course_index, list_student)
            case 3:
                list_course[course_index]["mark"] = del_mark(list_course, course_index, list_student)
            case 4:
                list_course[course_index]["mark"] = del_n_mark(list_course, course_index, list_student)
            case 5:
                list_course[course_index]["mark"] = del_all_elements(list_course[course_index]["mark"], 1)
            case 6:
                list_course[course_index]["mark"] = update_mark(list_course, course_index, list_student)
            case _:
                print("\tInvalid option!")


def add_mark(list_course, course_index, list_student):
    list_mark = list_course[course_index]["mark"]
    num_students = len(list_student)
    while True:
        print(f"""
        ADD MARK

[0] Exit""")

        try:
            student_selection = int(input("Enter student id: "))
        except ValueError:
            student_selection = -1
        if student_selection == 0:
            return list_mark
        student_index = student_selection - 1
        if 0 < student_selection <= num_students:
            lookup_result = mark_lookup(list_course, course_index, student_index)
            if lookup_result != "n/a":
                print("Already marked this student!")
                return list_mark

            list_mark += [{}]
            list_mark[-1] = {
                "student_id": student_selection,
                "mark": format(input_mark(), ".2f")
            }
            return list_mark
        else:
            print("\tInvalid option!")


def input_mark():
    while True:
        try:
            in_mark = float(input("Enter new mark (scale 20): "))
        except ValueError:
            in_mark = -1
        if 0 <= in_mark <= 20:
            return in_mark
        else:
            print("\tInvalid option!")


def add_n_mark(list_course, course_index, list_student):
    list_mark = list_course[course_index]["mark"]
    while True:
        try:
            times = int(input("Enter number of new marks ([0] to exit): "))
        except ValueError:
            times = -1
        if times == 0:
            return list_mark
        if times < 0 or times > len(list_student):
            print("\tInvalid input!")
        else:
            for i in range(times):
                print(f"\n\tEnter mark for the {ordinal(i+1)} student: ")
                list_mark = add_mark(list_course, course_index, list_student)
            break
    return list_mark


def del_mark(list_course, course_index, list_student):
    list_mark = list_course[course_index]["mark"]
    num_students = len(list_student)
    if list_no_element(list_mark, 2):
        return list_mark
    try:
        student_selection = int(input("Enter student id: "))
    except ValueError:
        student_selection = -1
    if student_selection == 0:
        return list_mark
    student_index = student_selection - 1
    if 0 < student_selection <= num_students:
        lookup_result = mark_lookup(list_course, course_index, student_index)
        if lookup_result == "n/a":
            print("Student not marked!")
            return list_mark

        print(f"Deleted mark of {get_name(list_student, student_index)}: {lookup_result[0]}.")
        del list_mark[lookup_result[1]]
        list_no_element(list_mark, 2)
        return list_mark
    else:
        print("\tInvalid option!")


def del_n_mark(list_course, course_index, list_student):
    list_mark = list_course[course_index]["mark"]
    while True:
        try:
            times = int(input("Enter number of marks to be deleted ([0] to exit): "))
        except ValueError:
            times = -1
        if times == 0:
            return list_mark
        if times < 0 or times > len(list_mark):
            print("\tInvalid input!")
        else:
            for i in range(times):
                list_mark = del_mark(list_course, course_index, list_student)
            break
    return list_mark


def update_mark(list_course, course_index, list_student):
    list_mark = list_course[course_index]["mark"]
    num_students = len(list_student)
    if list_no_element(list_mark, 2):
        return list_mark
    try:
        student_selection = int(input("Enter student id: "))
    except ValueError:
        student_selection = -1
    if student_selection == 0:
        return list_mark
    student_index = student_selection - 1
    if 0 < student_selection <= num_students:
        lookup_result = mark_lookup(list_course, course_index, student_index)
        if lookup_result == "n/a":
            print("Student not marked!")
            return list_mark

        print("[Update]", end="")
        list_mark[lookup_result[1]]["mark"] = format(input_mark(), ".2f")

        return list_mark
    else:
        print("\tInvalid option!")


def quick(list_course, list_student):
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
                list_course = add_course(list_course)
            case 4:
                if list_no_element(list_course, 1):
                    return list_course
                course_selection = print_list_get_element(list_course, 1)
                if course_selection == 0:
                    return list_course
                course_index = course_selection - 1

                list_course[course_index]["mark"] = add_mark(list_course, course_index, list_student)
            case 5:
                list_all_elements(list_course, 1)
            case 6:
                list_all_elements(list_student, 0)
            case 7:
                view_a_course(list_course, list_student)
            case _:
                print("\tInvalid option!")


def main():
    # init
    students = []
    courses = []

    home(students, courses)


if __name__ == "__main__":
    main()
