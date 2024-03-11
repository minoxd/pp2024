class Mark:
    def __init__(self, msid, mcid, mval=format(0, ".2f")):
        self.__msid = msid
        self.__mcid = mcid
        self.__mval = mval  # format(mark, ".2f")

    # getters
    def get_msid(self):
        return self.__msid

    def get_mcid(self):
        return self.__mcid

    def get_mval(self):
        return self.__mval

    # setters
    def set_mval(self):
        while True:
            try:
                in_mark = float(input("Enter new mark (scale 20): "))
            except ValueError:
                in_mark = -1
            if 0 <= in_mark <= 20:
                self.__mval = format(in_mark, ".2f")
                break
            else:
                print("Invalid option!")


