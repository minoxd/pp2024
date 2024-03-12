from pw4.Student import Student
from pw4.utils.list_no_element import list_no_element


def del_all_elements(the_list, mode):
    key = "yesyesyes"
    label1 = [
        "STUDENTS IN THE CLASS",
        "MARKS IN THE COURSE"
    ]
    while True:
        print(f"""
        WARNING: THIS PROCESS CANNOT BE UNDONE
        ARE YOU SURE YOU WANT TO DELETE ALL {label1[mode]}?

[0] Exit
[!] Type "{key}" to confirm the deletion
""")
        answer = input("Enter your answer: ")
        if answer == "0":
            return the_list
        if answer == key:
            list_no_element(the_list, mode)
            match mode:
                case 0:
                    delete = Student()
                    delete.delete_list_sid()
                    the_list = []
                case 1:
                    pass
            return the_list
        print("Invalid input!")


