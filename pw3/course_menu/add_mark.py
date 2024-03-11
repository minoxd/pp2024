from pw3.Mark import Mark
from pw3.course_menu.print_mark import print_mark


def add_mark(s_list, c_list, c_index, m_list):
    print("""
        ADD MARK
""")
    sid = print_mark(s_list, c_list, c_index, m_list, 2)
    if sid == -1:
        return m_list
    new_m = Mark(
        sid,
        c_list[c_index].get_cid()
    )
    new_m.set_mval()
    m_list.append(new_m)
    return m_list


