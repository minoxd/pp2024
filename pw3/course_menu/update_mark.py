from pw3.course_menu.print_mark import print_mark
from pw3.utils.list_no_element import list_no_element


def update_mark(s_list, c_list, c_index, m_list):
    cid = c_list[c_index].get_cid()
    if list_no_element(s_list, 0):
        return m_list
    print("""
        UPDATE MARK
""")
    sid = print_mark(s_list, c_list, c_index, m_list, 1)
    if sid == -1:
        return m_list

    name = next(name for name in s_list if name.get_sid() == sid)
    for m in m_list:
        if m.get_msid() == sid and m.get_mcid() == cid:
            m.set_mval()
    print(f"Updated mark of {name.get_sname()}")

    return m_list


