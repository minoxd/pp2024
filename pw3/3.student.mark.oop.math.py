import math
from datetime import date
import numpy as np


# todo private method
# todo when new course, add default marks for all student to m_list
# todo only change, no add mark because mark auto assigned
def home(s_list, c_list, m_list):
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
                return s_list, c_list, m_list
            case 1:
                s_list, m_list = student(s_list, m_list)
            case 2:
                s_list, c_list, m_list = course(s_list, c_list, m_list)
            case 3:
                s_list, c_list, m_list = quick(s_list, c_list, m_list)
            case _:
                print("Invalid option!")


def student(s_list, m_list):
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
                return s_list, m_list
            case 1:
                s_list = add_student(s_list)
            case 2:
                s_list = add_n_student(s_list)
            case 3:
                s_list, m_list = del_student(s_list, m_list)
            case 4:
                s_list, m_list = del_n_student(s_list, m_list)
            case 5:
                s_list = del_all_elements(s_list, 0)
            case 6:
                s_list = view_update_student(s_list)
            case 7:
                print_list_get_element(s_list, 0, False)
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


class Student:
    __list_sid: list = []
    __default_sid: str = ""
    __default_sname: str = "student_name"
    __default_sdob: date = date(1, 1, 1)
    __default_smark: list = []
    __default_gpa: float = math.floor(0 * 10) / 10

    def __init__(self):
        self.__sid: str = self.__default_sid
        self.__sname: str = self.__default_sname
        self.__sdob: date = self.__default_sdob
        self.__smark: list = self.__default_smark
        self.__gpa: float = self.__default_gpa

    # getters
    def get_list_sid(self):
        if len(self.__list_sid) == 0:
            print("No student id used yet!")
            return
        print("Used student ids: " + str(self.__list_sid))

    def get_sid(self):
        return self.__sid

    def get_sname(self):
        return self.__sname

    def get_sdob(self):
        return self.__sdob

    def get_smark(self, c_list, m_list):
        self.update_smark(c_list, m_list)
        return self.__smark

    def get_gpa(self, c_list, m_list):
        self.update_gpa(c_list, m_list)
        return self.__gpa

    # setters
    def append_list_sid(self, sid):
        self.__list_sid.append(sid)

    def remove_list_sid(self, sid):
        self.__list_sid.remove(sid)

    def delete_list_sid(self):
        self.__list_sid.clear()

    def set_sid(self):
        while True:
            try:
                self.get_list_sid()
                sid = input("Enter student id: ")
                if not sid:
                    print("\nStudent id cannot be blank!")
                    raise ValueError
                if sid in self.__list_sid:
                    print(f"\nID existed, try another one!")
                    raise ValueError
                self.append_list_sid(sid)
                break
            except ValueError:
                pass
        self.__sid = sid

    def set_sname(self):
        sname = input("Enter student name: ")
        if not sname:
            sname = self.__default_sname
        self.__sname = sname

    def set_sdob(self):
        while True:
            try:
                print("Enter student birthday: ")
                y = input("\tYear: ")
                m = input("\tMonth: ")
                d = input("\tDay: ")
                if not y and not m and not d:
                    sdob = self.__default_sdob
                    break
                sdob = date(int(y), int(m), int(d))
                break
            except ValueError as ve:
                print(f"\nInvalid input: {ve}!")
        self.__sdob = sdob

    def update_smark(self, c_list, m_list):
        """reset and get sorted mark of each course according to c_list (or list_cid)"""
        self.__smark.clear()
        list_cid = [c.get_cid() for c in c_list]
        for cid in list_cid:
            self.__smark.append(
                next(m.get_mval() for m in m_list if m.get_cid() == cid)
            )

    def update_gpa(self, c_list, m_list):
        """reset and calc new gpa based on new smark"""
        self.update_smark(c_list, m_list)

        numpy_smark = np.array([
            mval for mval in self.__smark
        ])
        numpy_cre = np.array([
            c.get_cre() for c in c_list
        ])
        self.__gpa = math.floor(np.sum(numpy_smark * numpy_cre) * 10) / 10


class Course:
    __list_cid: list = []
    __sum_cre: int = 0
    __default_cid: str = ""
    __default_cname: str = "course_name"
    __default_cre: int = 0

    def __init__(self):
        self.__cid = self.__default_cid
        self.__cname = self.__default_cname
        self.__cre = self.__default_cre

    # getters
    def get_list_cid(self):
        if len(self.__list_cid) == 0:
            print("No course id used yet!")
            return
        print("Used course ids: " + str(self.__list_cid))

    def get_sum_cre(self):
        return self.__sum_cre

    def get_cid(self):
        return self.__cid

    def get_cname(self):
        return self.__cname

    def get_cre(self):
        return self.__cre

    # setters
    def append_list_cid(self, cid):
        self.__list_cid.append(cid)

    def remove_list_cid(self, cid):
        self.__list_cid.remove(cid)

    def add_sum_cre(self, cre):
        self.__sum_cre += cre

    def minus_sum_cre(self, cre):
        self.__sum_cre -= cre

    def set_cid(self):
        while True:
            try:
                self.get_list_cid()
                cid = input("Enter course id: ")
                if not cid:
                    print("\nCourse id cannot be blank!")
                    raise ValueError
                if cid in self.__list_cid:
                    print(f"\nID existed, try another one!")
                    raise ValueError
                self.append_list_cid(cid)
                break
            except ValueError:
                pass
        self.__cid = cid

    def set_cname(self):
        cname = input("Enter course name: ")
        if not cname:
            cname = self.__default_cname
        self.__cname = cname

    def set_cre(self):
        while True:
            try:
                cre = input("Enter credit value: ")
                if not cre:
                    cre = self.__default_cre
                cre = int(cre)
                break
            except ValueError:
                print(f"\nInvalid input!")
        self.__cre = cre


class Mark:
    """Store locally in each student"""
    __default_mval: float = math.floor(0 * 10) / 10

    def __init__(self, mcid):
        self.__mcid = mcid
        self.__mval = self.__default_mval

    # getters
    def get_mcid(self):
        return self.__mcid

    def get_mval(self):
        return self.__mval

    # setters
    def set_mval(self):
        while True:
            try:
                mval = input("Enter new mark (scale 20): ")
                if not mval:
                    self.__mval = self.__default_mval
                    break
                mval = float(mval)
            except ValueError:
                mval = -1
            if 0 <= mval <= 20:
                self.__mval = math.floor(mval * 10) / 10
                break
            else:
                print("Invalid option!\n")


def main():
    # init
    s_list = []
    c_list = []
    m_list = []

    try:
        s_list, c_list, m_list = home(s_list, c_list, m_list)

    except EOFError as e:
        print(e)


if __name__ == "__main__":
    main()
