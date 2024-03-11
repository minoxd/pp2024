from pw3.Student import Student


def add_student(s_list):
    new_s = Student()
    new_s.set_sid()
    new_s.set_sname()
    new_s.set_sdob()
    s_list.append(new_s)
    return s_list


