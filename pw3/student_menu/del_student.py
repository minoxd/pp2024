from pw3.utils.get_student_name_id import get_student_name_id
from pw3.utils.list_no_element import list_no_element
from pw3.utils.print_list_get_element import print_list_get_element


def del_student(s_list, m_list):
    s_select = print_list_get_element(s_list, 0, True)
    if s_select == 0:
        return s_list
    s_index = s_select - 1

    print(f"Deleted {get_student_name_id(s_list, s_index)}.")
    sid = s_list[s_index].get_sid()
    # remove their marks
    their_mark = [m for m in m_list if m.get_msid() == sid]
    for i in their_mark:
        m_list.remove(i)
    # remove their sid from sid list
    s_list[s_index].remove_list_sid(sid)

    del s_list[s_index]
    list_no_element(s_list, 0)
    return s_list, m_list


