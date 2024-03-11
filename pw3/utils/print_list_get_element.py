from pw3.utils.get_course_name_id import get_course_name_id
from pw3.utils.get_element_false import get_element_false
from pw3.utils.get_element_true import get_element_true
from pw3.utils.get_student_name_id import get_student_name_id
from pw3.utils.list_no_element import list_no_element


def print_list_get_element(the_list: list, mode, get: bool):
    if list_no_element(the_list, mode):
        return 0
    label1 = [
        "STUDENT LIST",
        "COURSE LIST"
    ]
    func1 = [
        get_student_name_id,
        get_course_name_id
    ]
    if get:
        return get_element_true(the_list, mode, label1, func1)
    else:
        get_element_false(the_list, mode, label1, func1)


