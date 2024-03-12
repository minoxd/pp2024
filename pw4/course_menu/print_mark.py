from pw4.course_menu.addable import addable
from pw4.course_menu.updatable import updatable
from pw4.utils.list_no_element import list_no_element


def print_mark(s_list, c_list, c_index, m_list, mode):
    cid = c_list[c_index].get_cid()
    c_mark = [m for m in m_list if m.get_mcid() == cid]
    print("\tMark status:\t", end="")
    # if list_no_element(c_mark, 2):
    #     return
    if list_no_element(s_list, 0):
        return
    print(f"Marked {len(c_mark)}/{len(s_list)} students.\n")
    match mode:
        case 0:
            updatable(s_list, c_mark, 0)
            addable(s_list, c_mark, 0)
        case 1:
            return updatable(s_list, c_mark, 1)
        case 2:
            return addable(s_list, c_mark, 1)
        case 3:
            pass  # return updatable(s_list, c_mark, 2)


