def class_not_exist(cur_num_class):
    if cur_num_class is None or cur_num_class < 1:
        print("There is no class.")
        return True
    return False


def select_class(selection, cur_num_class, list_class):
    if class_not_exist(cur_num_class):
        return
    while True:
        print("""
        AVAILABLE CLASSES
        
[0] Exit""")
        for i in range(cur_num_class):
            print(f"[{i+1}] {list_class[i]}")
        print("")
        try:
            option = int(input("Enter class: "))
        except ValueError:
            print("Invalid option!")
            option = int(input("Enter class: "))
        if option == 0:
            selection = -1
            return
        if 0 < option <= cur_num_class:
            selection = option
            break
        print("Invalid option!")
    print("You selected", list_class[selection-1])


def new_class(cur_num_class, list_class):
    cur_num_class += 1
    s = "CLASS" + str(cur_num_class)
    list_class += [s]
    print("Added", list_class[cur_num_class - 1])
    return cur_num_class


def delete_class(cur_num_class, list_class):
    if class_not_exist(cur_num_class):
        return
    print("Deleted", list_class[cur_num_class - 1])
    del list_class[cur_num_class - 1]
    return cur_num_class - 1


def update_class(selection, cur_num_class, list_class):
    if class_not_exist(cur_num_class):
        return



def display(list_class):
    print(*list_class, sep="\t")

def home_option


def class_part(classes, num_class, selected_class):
    while True:
        print("""
        STUDENT MARK PROGRAM
        
[0] Exit
[1] Select class
[2] Add new class
[3] Delete most recent class
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
            case 3:
                num_class = delete_class(num_class, classes)
            case 4:
                update_class(selected_class, num_class, classes)
            case 5:
                display(classes)
            case _:
                print("Invalid option!")


def main():
    # init
    classes = []
    num_class = 0
    selected_class = -1

    home_option(classes, num_class, selected_class)


if __name__ == "__main__":
    main()
