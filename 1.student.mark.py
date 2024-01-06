from datetime import date


def class_not_exist(list_class):
    num_class = len(list_class)
    if num_class < 1:
        print("There is no class.")
        return True
    return False


def update_student(list_class):
    if class_not_exist(list_class):
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
        {get_name(list_class, class_selection - 1)}

[0] Exit
[1] Add a new student
[2] Add multiple students
[3] Delete the newest student
[4] Delete multiple students
[5] Delete all
[6] Change name of an existing student
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
                list_class[class_selection - 1] = add_student(list_class[class_selection - 1])
            case 2:
                return
            case 3:
                return
            case 4:
                return
            case _:
                print("Invalid option!")


def add_student(list_student):
    list_student += [{}]
    list_student[-1] = {
        "id": len(list_student),
        "name": str(input("Enter name: ")),
        "dob": get_dob()
    }
    return list_student


def get_dob():
    print("Please enter the birthday in the following order: year, month, day.")
    dob = date(
        year=int(input("Year: ")),
        month=int(input("Month: ")),
        day=int(input("Day: "))
    )
    return dob


def add_class(list_class):
    new_name = str(input("Enter class name (or leave a blank for default): "))
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


def check_exist(list_class, name):
    for i in range(len(list_class)):
        if name == list_class[i]["name"]:
            return True
    return False


def print_get_class_choice(list_class):
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
            print("Invalid option!")


def get_name(the_list, index):
    return the_list[index]["name"]


def delete_class(list_class):
    if class_not_exist(list_class):
        return list_class
    class_selection = print_get_class_choice(list_class)
    if class_selection == 0:
        return list_class
    print("Deleted", get_name(list_class, class_selection - 1))
    del list_class[class_selection - 1]
    return list_class


def display(list_class):
    if class_not_exist(list_class):
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


def class_student(list_class):
    while True:
        print("""
        CLASSES AND STUDENTS
        
[0] Exit
[1] Add a new class
[2] Delete a class
[3] Update student of a class
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
                list_class = delete_class(list_class)
            case 3:
                list_class = update_student(list_class)
            case 4:
                display(list_class)
            case _:
                print("Invalid option!")


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
                print("Invalid option!")


def main():
    # init
    classes = []

    home_option(classes)


if __name__ == "__main__":
    main()
