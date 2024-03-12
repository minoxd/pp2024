import math
from datetime import date


class Student:
    __list_sid = []

    def __init__(self):
        self.__sid = str
        self.__sname = str
        self.__sdob = date
        self.__smark = list

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

    def get_smark(self):
        return self.__smark

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
            sname = "student_name"
        self.__sname = sname

    def set_sdob(self):
        while True:
            try:
                print("Enter student birthday: ")
                y = input("\tYear: ")
                m = input("\tMonth: ")
                d = input("\tDay: ")
                if not y and not m and not d:
                    y = 1
                    m = 1
                    d = 1
                sdob = date(int(y), int(m), int(d))
                break
            except ValueError as ve:
                print(f"\nInvalid input: {ve}!")
        self.__sdob = sdob


class Course:
    __list_cid: list = []
    __sum_cre: int = 0

    def __init__(self):
        self.__cid = str
        self.__cname = str
        self.__cre = int

    # getters
    def get_list_cid(self):
        if len(self.__list_cid) == 0:
            print("No course id used yet!")
            return
        print("Used course ids: " + str(self.__list_cid))

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
            cname = "course_name"
        self.__cname = cname

    def set_cre(self):
        while True:
            try:
                cre = input("Enter credit value: ")
                if not cre:
                    cre = 0
                cre = int(cre)
                break
            except ValueError:
                print(f"\nInvalid input!")
        self.__cre = cre


class Mark:
    def __init__(self, mcid, mval=math.floor(0 * 10) / 10):
        self.__mcid = mcid
        self.__mval = mval

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
                    mval = float(0)
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

    try:
        s_list, c_list = home(s_list, c_list)

    except EOFError as e:
        print(e)


if __name__ == "__main__":
    main()
