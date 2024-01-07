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
[3] Update students of a class
[4] List all classes
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
                list_class = update_student(list_class)
            case 4:
                display(list_class)
            case _:
                print("\tInvalid option!")


def check_exist(list_class, name):
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
        while check_exist(list_class, new_name):
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


def print_get_class_choice(list_class):  # todo: combine with get student
    num_class = len(list_class)
    while True:
        print("""
        AVAILABLE CLASSES

[0] Exit""")
        for i in range(num_class):
            print(f"[{i + 1}] {get_name(list_class, i)}")
        print("")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            option = -1
        if 0 <= option <= num_class:
            return option
        else:
            print("\tInvalid option!")


def del_class(list_class):
    if list_no_element(list_class, 1):
        return list_class
    class_selection = print_get_class_choice(list_class)
    if class_selection == 0:
        return list_class
    print("Deleted", get_name(list_class, class_selection - 1))
    del list_class[class_selection - 1]
    return list_class


def update_student(list_class):
    if list_no_element(list_class, 1):
        return list_class
    class_selection = print_get_class_choice(list_class)
    if class_selection == 0:
        return list_class
    update_student_option(list_class, class_selection)
    return list_class


def update_student_option(list_class, class_selection):
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
[6] Update an existing student
[7] List all students
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
                return
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


def del_student(list_student):  # todo: need change
    if list_no_element(list_student, 2):
        return list_student
    class_selection = print_get_class_choice(list_student)
    if class_selection == 0:
        return list_student
    print("Deleted", get_name(list_student, class_selection - 1))
    del list_student[class_selection - 1]
    return list_student


def display(list_class):
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
