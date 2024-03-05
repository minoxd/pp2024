class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Course:

    def __init__(self, name):
        self.__cname = None
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_c_cname(self):
        return self.__cname

    def set_c_cname(self, newname):
        self.__cname = newname


class SM(Student, Course):
    __name = "he"

    def get_self_name(self):
        return self.__name

    def __init__(self, name):
        Student.__init__(self, name)

    @classmethod
    def init_course(cls, name):
        instance = cls.__new__(cls)
        Course.__init__(instance, name)

    def get_student_name(self):
        return Student.get_name(self)

    def get_course_name(self):
        return Course.get_name(self)

    def set_course_name(self, name):
        Course.set_name(self, name)

    def get_sm_cname(self):
        return Course.get_c_cname(self)

    def set_sm_cname(self, newname):
        Course.set_c_cname(self, newname)


sm = SM("hello")
print(sm.get_student_name())
sm.set_course_name("hi")
print(sm.get_course_name())
print(sm.get_self_name())
sm.set_sm_cname("hihihaha")
print(sm.get_sm_cname())
