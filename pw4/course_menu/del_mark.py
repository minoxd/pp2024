from pw4.course_menu.print_mark import print_mark
from pw4.utils.list_no_element import list_no_element


def del_mark(s_list, c_list, c_index, m_list):
    cid = c_list[c_index].get_cid()
    c_mark = [m for m in m_list if m.get_mcid() == cid]
    if list_no_element(s_list, 0):
        return m_list
    print("""
        DELETE MARK
""")
    sid = print_mark(s_list, c_list, c_index, m_list, 1)
    if sid == -1:
        return m_list
    who = next(m for m in c_mark if m.get_msid() == sid)
    name = next(name for name in s_list if name.get_sid() == sid)
    print(f"Removed mark from {name.get_sname()}")
    m_list.remove(who)

    return m_list


