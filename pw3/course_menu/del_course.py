from pw3.course_menu.del_all_mark import del_all_mark
from pw3.utils.get_course_name_id import get_course_name_id
from pw3.utils.list_no_element import list_no_element
from pw3.utils.print_list_get_element import print_list_get_element


def del_course(c_list, m_list):
    c_select = print_list_get_element(c_list, 1, True)
    if c_select == 0:
        return c_list
    c_index = c_select - 1

    m_list = del_all_mark(c_list, c_index, m_list)

    print(f"Deleted course: {get_course_name_id(c_list, c_index)}.")
    cid = c_list[c_index].get_cid()
    c_list[c_index].remove_list_cid(cid)

    del c_list[c_index]
    list_no_element(c_list, 1)
    return c_list, m_list


