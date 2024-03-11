from pw3.course_menu.del_mark import del_mark
from pw3.utils.ordinal import ordinal


def del_n_mark(s_list, c_list, c_index, m_list):
    max_time = 5
    while True:
        try:
            times = int(input("""
[0] Exit    
Enter number of marks to delete: """))
        except ValueError:
            times = -1
        if times == 0:
            return m_list
        if times < 0:
            print("Invalid input!")
        elif times > max_time:
            print(f"Maximum {max_time} at once.")
        else:
            for i in range(times):
                print(f"\n\tThe {ordinal(i + 1)} student to be deleted: ")
                m_list = del_mark(s_list, c_list, c_index, m_list)
            break
    return m_list


