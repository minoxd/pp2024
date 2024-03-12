class Course:
    __list_cid = []

    def __init__(self):
        self.__cid = ""
        self.__cname = ""

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
                if cid in self.__list_cid:
                    raise ValueError
                self.append_list_cid(cid)
                break
            except ValueError:
                print(f"\nID existed, try another one!")
        self.__cid = cid

    def set_cname(self):
        self.__cname = input("Enter course name: ")


