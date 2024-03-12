from pw4.utils.del_all_elements import del_all_elements


def del_all_mark(c_list, c_index, m_list):
    del_all_elements(m_list, 1)
    cid = c_list[c_index].get_cid()
    return [m for m in m_list if m.get_mcid() != cid]


