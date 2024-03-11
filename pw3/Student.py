from datetime import date


class Student:
    __list_sid = []

    def __init__(self):
        self.__sid = ""
        self.__sname = ""
        self.__sdob = date(1, 1, 1)

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


