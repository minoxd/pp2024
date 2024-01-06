def class_not_exist(list_class):
    num_class = len(list_class)
    if num_class < 1:
        print("There is no class.")
        return True
    return False


def update_student(list_class):
    if class_not_exist(list_class):
        return list_class
    num_class = len(list_class)
    while True:
        print("""
        AVAILABLE CLASSES
        
[0] Exit""")
        for i in range(num_class):
            print(f"[{i+1}] {list_class[i]}")
        print("")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid option!")
            option = int(input("Enter your choice: "))
        if option == 0:
            return list_class
        if 0 < option <= num_class:
            selection = option
            break
        print("Invalid option!")
    update_student_option(list_class, selection)
    return list_class


def update_student_option(list_class, selection):
    num_class = len(list_class)

    while True:
        print(f"""
        {list_class[selection - 1]}

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
            print("Invalid option!")
            option = int(input("Enter your choice: "))
        match option:
            case 0:
                return
            case 1:
                list_class[selection - 1] = add_student(list_class[selection - 1])
            case 2:
                return
            case 3:
                return
            case 4:
                return
            case _:
                print("Invalid option!")


def add_student(list_student):
    return list_student


def add_class(list_class):
    s = "CLASS" + str(len(list_class) + 1)
    list_class += [s]
    list_class[-1] = []
    print("Added", list_class[-1])
    return list_class


def delete_class(list_class):
    if class_not_exist(list_class):
        return list_class
    num_class = len(list_class)
    print("Deleted", list_class[num_class - 1])
    del list_class[num_class - 1]
    return list_class


def display(list_class):
    if class_not_exist(list_class):
        return
    num_class = len(list_class)
    if num_class == 1:
        print(f"\nThere is {num_class} class:")
        print(*list_class, sep="\t")
    else:
        print(f"\nThere is {num_class} classes:")
        print(*list_class, sep="\t")


def class_student(list_class):
    while True:
        print("""
        CLASSES AND STUDENTS
        
[0] Exit
[1] Add new class
[2] Delete newest class
[3] Update student of a class
[4] List all classes
""")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid option!")
            option = int(input("Enter your choice: "))
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
            print("Invalid option!")
            option = int(input("Enter your choice: "))
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
