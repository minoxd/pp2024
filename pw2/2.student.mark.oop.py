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
            selection = int(input("Enter your choice: "))
        except ValueError:
            selection = -1
        match selection:
            case 0:
                print("""
        THANK YOU FOR USING MY PROGRAMME!!""")
                return
            case 1:
                student(list_student)
            case 2:
                pass  # course(list_course, list_student)
            case 3:
                pass  # quick(list_course, list_student)
            case _:
                print("Invalid option!")


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
[6] View/Update an existing student
[7] List all students
""")
        try:
            selection = int(input("Enter your choice: "))
        except ValueError:
            selection = -1
        match selection:
            case 0:
                return
            case 1:
                pass  # list_student = add_student(list_student)
            case 2:
                pass  # list_student = add_n_student(list_student)
            case 3:
                pass  # list_student = del_student(list_student)
            case 4:
                pass  # list_student = del_n_student(list_student)
            case 5:
                pass  # list_student = del_all_elements(list_student, 0)
            case 6:
                pass  # list_student = view_update_student(list_student)
            case 7:
                pass  # list_all_elements(list_student, 0)
            case _:
                print("Invalid option!")


class Student:
    __list_sid = []

    def __init__(
            self,
            sid="default",
            sname="default",
            sdob=date(1, 1, 1)):
        self.__sid = sid
        Student.__list_sid.append(sid)
        self.__sname = sname
        self.__sdob = sdob

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
    def set_list_sid(self, list_sid):
        self.__list_sid = list_sid

    def set_sname(self, sname):
        self.__sname = sname

    def set_sdob(self, sdob):
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
    def __init__(self, sid, cid):
        self.__sid = sid
        self.__cid = cid
        self.__mark = format(0, ".2f")  # TODO round()


def main():
    # init
    list_student = []
    list_course = []
    # list_mark = []

    home(list_student, list_course)


if __name__ == "__main__":
    main()
