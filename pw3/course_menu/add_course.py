from pw3.Course import Course


def add_course(c_list):
    new_c = Course()
    new_c.set_cid()
    new_c.set_cname()
    c_list.append(new_c)
    return c_list


