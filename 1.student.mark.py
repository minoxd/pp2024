from datetime import date


def home_option(list_class):
    while True:
        print("""
        STUDENT MARK PROGRAM

[0] Exit
[1] Classes & Students
[2] Courses
[3] Marking
[4] Quick options
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
                class_student(list_class)
            case 2:
                return
            case 3:
                return
            case 4:
                return
            case _:
                print("\tInvalid option!")


def class_student(list_class):
    while True:
        print("""
        CLASSES AND STUDENTS

[0] Exit
[1] Add a new class
[2] Delete a class
[3] View details of a class
[4] Update a class
[5] List all classes
""")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            option = -1
        match option:
            case 0:
                return
            case 1:
                list_class = add_class(list_class)
            case 2:
                list_class = del_class(list_class)
            case 3:
                display_class_details(list_class)
            case 4:
                list_class = update_class(list_class)
            case 5:
                display_list_class(list_class)
            case _:
                print("\tInvalid option!")


def check_auto_name_exist(list_class, name):
    for i in range(len(list_class)):
        if name == list_class[i]["name"]:
            return True
    return False


def get_name(the_list, index):
    return the_list[index]["name"]


def add_class(list_class):
    new_name = str(input("Enter class name (or leave a blank): "))
    if new_name == "":
        new_name = "unnamed"
        while check_auto_name_exist(list_class, new_name):
            new_name += "*"
    list_class += [{}]
    list_class[-1] = {
        "name": new_name,
        "student": []
    }
    print("Added", get_name(list_class, -1))
    return list_class


def list_no_element(the_list, class_or_student: int):
    num_element = len(the_list)
    if num_element < 1:
        print(f"There is no {["class", "student"][class_or_student-1]}.")
        return True
    return False


def print_get_class_or_student_choice(the_list, class_or_student: int):
    num_element = len(the_list)
    while True:
        print(f"""
        {["AVAILABLE CLASSES", "STUDENT LIST"][class_or_student-1]}

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


def confirm_del(num_student):
    while True:
        try:
            option = str(input(f"There are {num_student} students in the class.\nAre you sure you want to delete (y/N): ")).lower()
        except ValueError:
            option = -1
        match option:
            case "y" | "yes":
                return True
            case "n" | "no":
                return False
            case _:
                print("\tInvalid option!")


def del_class(list_class):
    if list_no_element(list_class, 1):
        return list_class
    class_selection = print_get_class_or_student_choice(list_class, 1)
    if class_selection == 0:
        return list_class
    num_student = len(list_class[class_selection - 1]["student"])
    if num_student:
        if not confirm_del(num_student):
            print("Deletion cancelled!")
            return list_class
    print(f"Deleted {get_name(list_class, class_selection - 1)} with {num_student} students.")
    del list_class[class_selection - 1]
    if len(list_class) == 0:
        print("There is no class left.")
    return list_class


def list_all_students(list_class, class_selection):
    num_student = len(list_class[class_selection - 1]["student"])
    print(f"""
            Class: {get_name(list_class, class_selection - 1)}

        Number of students: {num_student}
        List of students:""")
    for i in range(num_student):
        print(f"{get_name(list_class[class_selection - 1]["student"], i)}")
    return


def display_class_details(list_class):
    if list_no_element(list_class, 1):
        return
    class_selection = print_get_class_or_student_choice(list_class, 1)
    if class_selection == 0:
        return
    list_all_students(list_class, class_selection)
    return


def update_class(list_class):
    if list_no_element(list_class, 1):
        return list_class
    class_selection = print_get_class_or_student_choice(list_class, 1)
    if class_selection == 0:
        return list_class
    update_class_options(list_class, class_selection)
    return list_class


def update_class_options(list_class, class_selection):
    num_class = len(list_class)

    while True:
        print(f"""
        Class: {get_name(list_class, class_selection - 1)}

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
                list_class[class_selection - 1]["student"] = add_student(list_class[class_selection - 1]["student"])
            case 2:
                list_class[class_selection - 1]["student"] = add_n_student(list_class[class_selection - 1]["student"])
            case 3:
                list_class[class_selection - 1]["student"] = del_student(list_class[class_selection - 1]["student"])
            case 4:
                list_class[class_selection - 1]["student"] = del_n_student(list_class[class_selection - 1]["student"])
            case 5:
                list_class[class_selection - 1]["student"] = del_all_students(list_class[class_selection - 1]["student"],
                                                                              list_class[class_selection - 1]["name"])
            case 6:
                view_a_student(list_class[class_selection - 1]["student"])
            case 7:
                list_class[class_selection - 1]["student"] = update_student(list_class[class_selection - 1]["student"])
            case 8:
                list_all_students(list_class, class_selection)
            case _:
                print("\tInvalid option!")


def add_student(list_student):
    list_student += [{}]
    list_student[-1] = {
        "id": len(list_student),
        "name": str(input("Enter name: ")),
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


def ordinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix


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
                print(f"\n\tEnter information for the {ordinal(i+1)} student: ")
                list_student = add_student(list_student)
            break
    return list_student


def del_student(list_student):
    num_students = len(list_student)
    if list_no_element(list_student, 2):
        return list_student
    student_selection = print_get_class_or_student_choice(list_student, 2)
    if student_selection == 0:
        return list_student
    print(f"Deleted {get_name(list_student, student_selection - 1)}.")
    del list_student[student_selection - 1]
    if len(list_student) == 0:
        print("There is no student left.")
    for i in range(num_students - student_selection):
        list_student[student_selection - 1 + i]["id"] -= 1
    return list_student


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


def del_all_students(list_student, class_name):
    key = "yesyesyes"
    while True:
        print(f"""
        WARNING: THIS PROCESS CANNOT BE UNDONE
        ARE YOU SURE YOU WANT TO DELETE ALL STUDENTS IN {class_name}

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
    if list_no_element(list_student, 2):
        return
    student_selection = print_get_class_or_student_choice(list_student, 2)
    if student_selection == 0:
        return
    print(f"""
    Student:\t\t\t{get_name(list_student, student_selection - 1)}
    ID:\t\t\t\t\t{list_student[student_selection - 1]["id"]}
    DOB (YYYY-MM-DD):\t{list_student[student_selection - 1]["dob"]}""")
    return


def update_student(list_student):  # TODO
    num_students = len(list_student)
    if list_no_element(list_student, 2):
        return list_student
    student_selection = print_get_class_or_student_choice(list_student, 2)
    if student_selection == 0:
        return list_student

    while True:
        print(f"""
        SELECTED STUDENT
    Student:\t\t\t{get_name(list_student, student_selection - 1)}
    ID:\t\t\t\t\t{list_student[student_selection - 1]["id"]}
    DOB (YYYY-MM-DD):\t{list_student[student_selection - 1]["dob"]}

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


def display_list_class(list_class):
    if list_no_element(list_class, 1):
        return
    num_class = len(list_class)
    if num_class == 1:
        print(f"\nThere is {num_class} class:")
        print(f"{get_name(list_class, 0)}")
    else:
        print(f"\nThere is {num_class} classes:")
        for i in range(num_class):
            print(f"{get_name(list_class, i)}")
        print()


def main():
    # init
    classes = []

    home_option(classes)


if __name__ == "__main__":
    main()
