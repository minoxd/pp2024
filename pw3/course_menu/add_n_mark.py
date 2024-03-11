from pw3.course_menu.add_mark import add_mark
from pw3.utils.ordinal import ordinal


def add_n_mark(s_list, c_list, c_index, m_list):
    max_time = 5
    while True:
        try:
            times = int(input("""
[0] Exit    
Enter number of new marks: """))
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
                print(f"\n\tEnter mark for the {ordinal(i + 1)} student: ")
                m_list = add_mark(s_list, c_list, c_index, m_list)
            break
    return m_list


