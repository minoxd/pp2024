def select_class(selection, cur_num_class, list_class):
    if cur_num_class == 0:
        print("There is no class.")
        return
    while True:
        print("""
        AVAILABLE CLASSES

[0] Exit
[1] Select class
[2] Add new class
[3] Delete recent class
[4] Update class
[5] Display class
        """)
        try:
            option = int(input("Enter class: "))
        except ValueError:
            print("Invalid option!")
            option = int(input("Enter class: "))
        if option == 0:
            return
        if 0 < option < cur_num_class:
            selection = option
            return
    print("You selected ", list_class[selection-1])


def new_class(cur_num_class, list_class):
    cur_num_class += 1
    s = "CLASS" + str(cur_num_class)
    list_class += [s]
    print("Added", list_class[cur_num_class-1])
    return cur_num_class


def makeClassOf(numOfStudents):
    for i in range(numOfStudents):
        studentID = input("Enter Student ID: ")
        studentName = input("Enter Student Name: ")
        studentDOB = input("Enter Student DOB: ")


def home_option(classes, num_class, selected_class):
    while True:
        print("""
        STUDENT MARK PROGRAM
        
[0] Exit
[1] Select class
[2] Add new class
[3] Delete recent class
[4] Update class
[5] Display class
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
                select_class(selected_class, num_class, classes)
            case 2:
                num_class = new_class(num_class, classes)
            case _:
                print("Invalid option!")


def main():
    # init
    classes = []
    num_class = 0
    selected_class = -1

    home_option(classes, num_class, selected_class)


    print(*classes, sep=" ")


if __name__ == "__main__":
    main()
