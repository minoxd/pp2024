from datetime import date


def home(s_list, c_list):
    while True:
        print("""
        STUDENT MARK PROGRAM

[0] Exit
[1] Students
[2] Courses
[3] Quick options
""")
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                print("""
        THANK YOU FOR USING MY PROGRAMME!!""")
                return
            case 1:
                student(s_list)
            case 2:
                pass  # course(list_course, list_student)
            case 3:
                pass  # quick(list_course, list_student)
            case _:
                print("Invalid option!")


def student(s_list):
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
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                return
            case 1:
                s_list = add_student(s_list)
            case 2:
                s_list = add_n_student(s_list)
            case 3:
                s_list = del_student(s_list)
            case 4:
                s_list = del_n_student(s_list)
            case 5:
                pass  # list_student = del_all_elements(list_student, 0)
            case 6:
                pass  # list_student = view_update_student(list_student)
            case 7:
                pass  # list_all_elements(list_student, 0)
            case _:
                print("Invalid option!")


def add_student(s_list):
    new_s = Student()
    new_s.set_sid()
    new_s.set_sname()
    new_s.set_sdob()
    s_list.append(new_s)
    return s_list


def add_n_student(s_list):
    while True:
        try:
            times = int(input("""
[0] Exit
Enter number of new students: """))
        except ValueError:
            times = -1
        if times == 0:
            return s_list
        if times < 0:
            print("Invalid input!")
        else:
            for i in range(times):
                print(f"\nEnter information for the {ordinal(i + 1)} student: ")
                s_list = add_student(s_list)
            break
    return s_list


def ordinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix


def del_student(s_list):
    s_select = print_list_get_element(s_list, 0, True)
    if s_select == 0:
        return s_list
    s_index = s_select - 1

    print(f"Deleted {get_student_name_id(s_list, s_index)}.")
    sid = s_list[s_index].get_sid()
    s_list[s_index].remove_list_sid(sid)

    del s_list[s_index]
    list_no_element(s_list, 0)
    return s_list


def print_list_get_element(the_list: list, mode, get: bool):
    if list_no_element(the_list, mode):
        return 0
    label1 = [
        "STUDENT LIST",
        # "COURSE LIST"
    ]
    func1 = [
        get_student_name_id,
        # get_course_name_id
    ]
    if get:
        return get_element_true(the_list, mode, label1, func1)
    else:
        get_element_false(the_list, mode, label1, func1)


def list_no_element(the_list, mode):
    num_element = len(the_list)
    label1 = [
        "student in the class",
        # "course available",
        # "mark"
    ]
    if num_element < 1:
        print(f"There is no {label1[mode]}.")
        return True
    return False


def get_element_true(the_list, mode, label1, func1):
    num_element = len(the_list)
    while True:
        print(f"""
        {label1[mode]}

[0] Exit""")
        for i in range(num_element):
            name_id = func1[mode](the_list, i)
            print(f"[{i + 1}] {name_id}")
        print()
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        if 0 <= select <= num_element:
            return select
        else:
            print("Invalid option!")


def get_element_false(the_list, mode,  label1, func1):
    num_element = len(the_list)
    label2 = [
        "students",
        # "courses"
    ]
    print(f"""
        {label1[mode]}

    Number of {label2[mode]}: {num_element}
    Listing all {label2[mode]}:""")
    for i in range(num_element):
        name_id = func1[mode](the_list, i)
        print(f"{name_id}")
    return


def get_student_name_id(s_list, s_index):
    the_name = s_list[s_index].get_sname()
    the_id = s_list[s_index].get_sid()
    return f"{the_name} (ID: {the_id})"


def get_course_name_id(c_list, c_index):
    the_name = c_list[c_index].get_cname()
    the_id = c_list[c_index].get_cid()
    return f"{the_name} (ID: {the_id})"


def del_n_student(s_list):
    while True:
        try:
            times = int(input("""
[0] Exit
Enter number of students to be deleted: """))
        except ValueError:
            times = -1
        if times == 0:
            return s_list
        if times < 0 or times > len(s_list):
            print("Invalid input!")
        else:
            for i in range(times):
                print(f"The {ordinal(i + 1)} student to be deleted: ")
                s_list = del_student(s_list)
            break
    return s_list


class Student:
    __list_sid = []

    def __init__(self):
        self.__sid = ""
        self.__sname = ""
        self.__sdob = date(1, 1, 1)

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
    def append_list_sid(self, sid):
        self.__list_sid.append(sid)

    def remove_list_sid(self, sid):
        self.__list_sid.remove(sid)

    def set_sid(self):
        while True:
            try:
                sid = input("Enter student id: ")
                if sid in self.__list_sid:
                    raise ValueError
                self.append_list_sid(sid)
                break
            except ValueError:
                print(f"\nID existed, try another one!")
        self.__sid = sid

    def set_sname(self):
        self.__sname = input("Enter student name: ")

    def set_sdob(self):
        while True:
            try:
                print("Enter student birthday: ")
                sdob = date(
                    year=int(input("\tYear: ")),
                    month=int(input("\tMonth: ")),
                    day=int(input("\tDay: "))
                )
                break
            except ValueError as ve:
                print(f"\nInvalid input: {ve}!")
        self.__sdob = sdob


class Course:
    __list_cid = []

    def __init__(self, cid, cname):
        self.__cid = cid
        Course.__list_cid.append(cid)
        self.__cname = cname

    # getters
    def get_list_cid(self):
        return self.__list_cid

    def get_cid(self):
        return self.__cid

    def get_cname(self):
        return self.__cname

    # setters
    def set_list_cid(self, list_cid):
        self.__list_cid = list_cid

    def set_cname(self, cname):
        self.__cname = cname


class Mark:
    def __init__(self, sid, cid, mark=format(0, ".2f")):
        self.__sid = sid
        self.__cid = cid
        self.__mark = mark  # format(mark, ".2f")


def main():
    # init
    s_list = []
    c_list = []
    # m_list = []

    home(s_list, c_list)
    for i in s_list:
        print(i.get_sname())


if __name__ == "__main__":
    main()
