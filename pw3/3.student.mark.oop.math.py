import curses
from curses import wrapper
from curses.textpad import Textbox
import math
import numpy as np
import time
from datetime import date
# todo len string <=10 and len list <=20


def test_screen(stdscr):
    while True:
        try:
            pad = curses.newpad(25, 50)
            stdscr.refresh()

            for i in range(1249):
                pad.addstr(" ")

            for i in range(50):
                stdscr.clear()
                stdscr.refresh()
                pad.refresh(0, 0, 0, 0, 0 + i, 0 + i)
                time.sleep(.0001)
            stdscr.clear()
            stdscr.refresh()
            height, width = stdscr.getmaxyx()
            label = [
                "Try not to adjust the size",
                "of the window while using!"
            ]
            for i in range(2):
                stdscr.addstr(height//2-1 + i, width//2 - len(label[i])//2, label[i], curses.color_pair(1))
            stdscr.refresh()
            stdscr.getch()
            del pad
            break
        except curses.error:
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(0, 0, "Please make your window larger!", curses.color_pair(1))
            stdscr.addstr(1, 0, "Ideally at least 50x20", curses.color_pair(2))
            stdscr.getch()


def home(stdscr, s_list, c_list, m_list):
    stdscr.clear()
    stdscr.refresh()
    y_mode = 0
    while True:
        curses_home(stdscr)
        try:
            select = int(ask_menu_choice(y_mode))
        except ValueError:
            select = -1
        match select:
            case 0:
                curses_home_exit(stdscr)
                return s_list, c_list, m_list
            case 1:
                s_list, c_list, m_list = student(stdscr, s_list, c_list, m_list)
            case 2:
                s_list, c_list, m_list = course(stdscr, s_list, c_list, m_list)
            case 3:
                s_list, c_list, m_list = quick(stdscr, s_list, c_list, m_list)
            case _:
                invalid_choice(stdscr, y_mode)


def curses_home(stdscr):
    option = [
        "Exit",
        "Students",
        "Courses",
        "Quick options"
    ]
    stdscr.clear()
    stdscr.addstr(1, 8, "STUDENT MARK PROGRAM")
    for i in range(4):
        stdscr.addstr(3 + i, 0, f"[{i}] {option[i]}")

    stdscr.addstr(8, 0, "Enter your choice: ")
    stdscr.refresh()


def ask_menu_choice(y_mode):
    y = y_choice(y_mode)
    win = curses.newwin(1, 2, y, 19)
    box = Textbox(win)
    curses.curs_set(1)
    box.edit()
    curses.curs_set(0)
    select = box.gather()
    return select


def curses_home_exit(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    label = "THANK YOU FOR USING MY PROGRAM!!!"
    stdscr.addstr(height // 2 - 1, width // 2 - len(label) // 2, label, curses.color_pair(2))
    stdscr.refresh()
    stdscr.getch()


def invalid_choice(stdscr, y_mode):
    y = y_choice(y_mode)
    stdscr.addstr(y, 0, "Enter your choice: ", curses.color_pair(1))
    stdscr.refresh()
    time.sleep(.1)


def y_choice(y_mode):
    match y_mode:
        case 0:  # home
            y = 8
        case 1:  # student
            y = 13
        case 2:  # n_items
            y = 6
        case 3:  # once
            y = 3
        case _:
            y = -1
    return y


def student(stdscr, s_list, c_list, m_list):
    stdscr.clear()
    stdscr.refresh()
    y_mode = 1
    while True:
        curses_student(stdscr)
        try:
            select = int(ask_menu_choice(y_mode))
        except ValueError:
            select = -1
        match select:
            case 0:
                return s_list, c_list, m_list
            case 1:
                s_list, m_list = add_student(stdscr, s_list, c_list, m_list)
            case 2:
                s_list, m_list = add_n_student(stdscr, s_list, c_list, m_list)
            case 3:
                s_list, m_list = del_student(stdscr, s_list, m_list)
            case 4:
                s_list, m_list = del_n_student(stdscr, s_list, m_list)
            case 5:
                s_list = del_all_elements(stdscr, s_list, 0)
                m_list = []
            case 6:
                s_list, c_list, m_list = view_update_student(stdscr, s_list, c_list, m_list)
            case 7:
                print_list_get_element(stdscr, s_list, 0, False)
            case 8:
                obj = Student()
                obj.get_list_gpa_desc(stdscr, s_list, c_list, m_list)
            case _:
                invalid_choice(stdscr, y_mode)


def curses_student(stdscr):
    option = [
        "Exit",
        "Add a new student",
        "Add multiple students",
        "Delete a student",
        "Delete multiple students",
        "Delete all",
        "View/Update an existing student",
        "List all students",
        "Sort student by GPA descending",
    ]
    stdscr.clear()
    stdscr.addstr(1, 8, "STUDENT LIST")
    for i in range(9):
        stdscr.addstr(3 + i, 0, f"[{i}] {option[i]}")

    stdscr.addstr(13, 0, "Enter your choice: ")
    stdscr.refresh()


def add_student(stdscr, s_list, c_list, m_list, y=y_choice(3)):
    stdscr.addstr(1, 8, "STUDENT LIST")
    new_s = Student()
    new_s.set_sid(stdscr, y)
    new_s.set_sname(stdscr, y)
    new_s.set_sdob(stdscr, y)
    # init mark of all student for new course
    for c in c_list:
        new_m = Mark(
            new_s.get_sid(),
            c.get_cid()
        )
        m_list.append(new_m)
    s_list.append(new_s)
    return s_list, m_list


def add_n_student(stdscr, s_list, c_list, m_list):
    stdscr.refresh()
    y = y_choice(2)
    label_mode = 0
    while True:
        curses_n_item(stdscr, y, label_mode)
        try:
            times = int(curses_time_item(y, 0))
        except ValueError:
            times = -1
        if times == 0:
            return s_list, m_list
        if times < 0:
            invalid_n_item(stdscr, y, label_mode)
        else:
            for i in range(times):
                curses_ordinal(stdscr, ordinal(i + 1), label_mode)
                s_list, m_list = add_student(stdscr, s_list, c_list, m_list, y)
            break
    return s_list, m_list


def curses_n_item(stdscr, y, label_mode):
    y -= 1
    label1 = [
        "STUDENT LIST"
    ]
    label2 = [
        "Enter number of new students: ",
    ]
    stdscr.clear()
    stdscr.addstr(1, 8, label1[0])
    stdscr.addstr(3, 0, "[0] Exit")
    stdscr.addstr(y, 0, label2[label_mode])
    stdscr.refresh()


def curses_time_item(y, label_mode):
    y -= 1
    label = [
        "Enter number of new students: ",
    ]
    win = curses.newwin(1, 30, y, len(label[label_mode]))
    box = Textbox(win)
    curses.curs_set(1)
    box.edit()
    curses.curs_set(0)
    select = box.gather()
    return select


def invalid_n_item(stdscr, y, label_mode):
    y -= 1
    label = [
        "Enter number of new students: "
    ]
    stdscr.addstr(y, 0, label[label_mode], curses.color_pair(1))
    stdscr.refresh()
    time.sleep(.1)


def curses_ordinal(stdscr, oordinal, mode):
    label = [
        f"Enter information for the {oordinal} student: ",
    ]
    for i in range(50):
        stdscr.addstr(7, i, " ")
    stdscr.addstr(7, 0, label[mode])
    stdscr.refresh()


def ordinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix


def del_student(stdscr, s_list, m_list):
    s_select = print_list_get_element(stdscr, s_list, 0, True)
    if s_select == 0:
        return s_list, m_list
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
    list_no_element(stdscr, s_list, 0)
    return s_list, m_list


def print_list_get_element(stdscr, the_list: list, mode, get: bool):
    if list_no_element(stdscr, the_list, mode):
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
        return get_element_true(stdscr, the_list, mode, label1, func1)
    else:
        get_element_false(stdscr, the_list, mode, label1, func1)


def list_no_element(stdscr, the_list, mode):
    num_element = len(the_list)
    label1 = [
        "student in the class",
        "course available",
        "mark"
    ]
    if num_element < 1:
        print(f"There is no {label1[mode]}.")
        return True
    return False


def get_student_name_id(s_list, s_index):
    the_name = s_list[s_index].get_sname()
    the_id = s_list[s_index].get_sid()
    return f"{the_name} (ID: {the_id})"


def get_course_name_id(c_list, c_index):
    the_name = c_list[c_index].get_cname()
    the_id = c_list[c_index].get_cid()
    return f"{the_name} (ID: {the_id})"


def get_element_true(stdscr, the_list, mode, label1, func1):
    num_element = len(the_list)
    while True:
        print(f"""
        {label1[mode]}

[0] Exit""")
        for i in range(num_element):
            name_id = func1[mode](the_list, i)
            print(f"[{i + 1}] {name_id}")
        print()
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        if 0 <= select <= num_element:
            return select
        else:
            print("Invalid option!")


def get_element_false(stdscr, the_list, mode, label1, func1):
    num_element = len(the_list)
    label2 = [
        "students",
        "courses"
    ]
    print(f"""
        {label1[mode]}

    Number of {label2[mode]}: {num_element}
    Listing all {label2[mode]}:""")
    for i in range(num_element):
        name_id = func1[mode](the_list, i)
        print(f"{name_id}")
    return


def del_n_student(stdscr, s_list, m_list):
    while True:
        try:
            times = int(input("""
[0] Exit
Enter number of students to be deleted: """))
        except ValueError:
            times = -1
        if times == 0:
            return s_list, m_list
        if times < 0 or times > len(s_list):
            print("Invalid input!")
        else:
            for i in range(times):
                print(f"The {ordinal(i + 1)} student to be deleted: ")
                s_list = del_student(stdscr, s_list, m_list)
            break
    return s_list, m_list


def del_all_elements(stdscr, the_list, mode):
    key = "yesyesyes"
    label1 = [
        "STUDENTS IN THE CLASS",
        "MARKS IN THE COURSE"
    ]
    while True:
        print(f"""
        WARNING: THIS PROCESS CANNOT BE UNDONE
        ARE YOU SURE YOU WANT TO DELETE ALL {label1[mode]}?

[0] Exit
[!] Type "{key}" to confirm the deletion
""")
        answer = input("Enter your answer: ")
        if answer == "0":
            return the_list
        if answer == key:
            list_no_element(stdscr, the_list, mode)
            match mode:
                case 0:
                    delete = Student()
                    delete.delete_list_sid()
                    the_list = []
                    # if no student then no mark
                    # all mark are deleted in the parent function
                case 1:
                    pass
            return the_list
        print("Invalid input!")


def view_update_student(stdscr, s_list, c_list, m_list):
    s_select = print_list_get_element(stdscr, s_list, 0, True)
    if s_select == 0:
        return s_list, c_list, m_list
    s_index = s_select - 1

    while True:
        obj = Course()
        sum_cre = obj.get_sum_cre(c_list)

        print(f"""
        SELECTED STUDENT
        
    Student:            {get_student_name_id(s_list, s_index)}
    DOB (YYYY-MM-DD):   {s_list[s_index].get_sdob()}
    GPA:                {s_list[s_index].get_gpa(c_list, m_list)}
    Total credits:      {sum_cre}
    Course mark:
""")
        print_s_mark(stdscr, s_list, s_index, c_list, m_list)

        print("""[0] Exit
[1] Change name
[2] Change dob
[3] Change course (mark)
""")
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                return s_list, c_list, m_list
            case 1:
                s_list[s_index].set_sname(stdscr)
            case 2:
                s_list[s_index].set_sdob(stdscr)
            case 3:
                s_list, c_list, m_list = course(stdscr, s_list, c_list, m_list)
            case _:
                print("Invalid option!")


def print_s_mark(stdscr, s_list, s_index, c_list, m_list):
    sid = s_list[s_index].get_sid()
    s_mark = [m for m in m_list if m.get_msid() == sid]
    for c in c_list:
        cid = c.get_cid()
        cname = c.get_cname()
        mark = next(m.get_mval() for m in s_mark if m.get_mcid() == cid)
        print(f"{cname} (ID: {cid}): {mark}")


def course(stdscr, s_list, c_list, m_list):
    while True:
        print(f"""
        COURSE LIST

[0] Exit
[1] Add a new course
[2] Delete a course
[3] View/Update an existing course
[4] List all courses
""")
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                return s_list, c_list, m_list
            case 1:
                c_list, m_list = add_course(stdscr, s_list, c_list, m_list)
            case 2:
                c_list, m_list = del_course(stdscr, c_list, m_list)
            case 3:
                c_list, m_list = view_update_course(stdscr, s_list, c_list, m_list)
            case 4:
                print_list_get_element(stdscr, c_list, 1, False)
            case _:
                print("Invalid option!")


def add_course(stdscr, s_list, c_list, m_list):
    new_c = Course()
    new_c.set_cid(stdscr)
    new_c.set_cname(stdscr)
    new_c.set_cre(stdscr)
    c_list.append(new_c)
    # init mark of all student for new course
    for s in s_list:
        new_m = Mark(
            s.get_sid(),
            new_c.get_cid()
        )
        m_list.append(new_m)
    return c_list, m_list


def del_course(stdscr, c_list, m_list):
    c_select = print_list_get_element(stdscr, c_list, 1, True)
    if c_select == 0:
        return c_list, m_list
    c_index = c_select - 1

    m_list = del_all_mark(stdscr, c_list, c_index, m_list)

    print(f"Deleted course: {get_course_name_id(c_list, c_index)}.")
    # remove cid from cid list
    cid = c_list[c_index].get_cid()
    c_list[c_index].remove_list_cid(cid)
    # remove obj
    del c_list[c_index]
    return c_list, m_list


def del_all_mark(stdscr, c_list, c_index, m_list):
    del_all_elements(stdscr, m_list, 1)
    cid = c_list[c_index].get_cid()
    return [m for m in m_list if m.get_mcid() != cid]


def view_update_course(stdscr, s_list, c_list, m_list):
    c_select = print_list_get_element(stdscr, c_list, 1, True)
    if c_select == 0:
        return c_list, m_list
    c_index = c_select - 1

    while True:
        print(f"""
        SELECTED COURSE
    Course:             {get_course_name_id(c_list, c_index)}
    Credits:            {c_list[c_index].get_cre()}""")
        c_mark_status(stdscr, s_list, c_list, c_index, m_list, 0)

        print("""
[0] Exit
[1] Change course name
[2] Change number of credits
[3] Update mark
""")
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                return c_list, m_list
            case 1:
                c_list[c_index].set_cname(stdscr)
            case 2:
                c_list[c_index].set_cre(stdscr)
            case 3:
                m_list = update_mark(stdscr, s_list, c_list, c_index, m_list)
            case _:
                print("Invalid option!")


def c_mark_status(stdscr, s_list, c_list, c_index, m_list, mode):
    # get list mark obj of selected course
    cid = c_list[c_index].get_cid()
    c_mark = [m for m in m_list if m.get_mcid() == cid]
    # print mark of selected course
    print(f"    Student enrolled:   {len(s_list)}\n")
    match mode:
        case 0:
            c_mark_print_get(stdscr, s_list, c_mark, False)
        case 1:
            return c_mark_print_get(stdscr, s_list, c_mark, True)


def c_mark_print_get(stdscr, s_list, c_mark, mode: bool):
    match mode:
        case False:
            for s in s_list:
                mark_obj = next(m for m in c_mark if m.get_msid() == s.get_sid())
                print(f"{s.get_sname()} (ID: {s.get_sid()}): {mark_obj.get_mval()}")
        case True:
            while True:
                print("[0] Exit")
                for i in range(len(s_list)):
                    mark_obj = next(m for m in c_mark if m.get_msid() == s_list[i].get_sid())
                    print(f"[{i + 1}] {s_list[i].get_sname()} (ID: {s_list[i].get_sid()}): {mark_obj.get_mval()}")
                try:
                    s_select = int(input("Enter your choice: "))
                except ValueError:
                    s_select = -1
                if 0 <= s_select <= len(s_list):
                    s_index = s_select - 1
                    if s_index == -1:
                        return -1
                    # return selected student's id
                    return s_list[s_index].get_sid()
                else:
                    print("Invalid option!\n")


def update_mark(stdscr, s_list, c_list, c_index, m_list):
    cid = c_list[c_index].get_cid()
    if list_no_element(stdscr, s_list, 0):
        return m_list
    print("""
        UPDATE MARK
""")
    sid = c_mark_status(stdscr, s_list, c_list, c_index, m_list, 1)
    if sid == -1:
        return m_list

    s_select = next(s for s in s_list if s.get_sid() == sid)
    for m in m_list:
        if m.get_msid() == sid and m.get_mcid() == cid:
            m.set_mval(stdscr)
    print(f"Updated mark of {s_select.get_sname()}")

    return m_list


def quick(stdscr, s_list, c_list, m_list):
    while True:
        print("""
        QUICK OPTIONS

[0] Exit

    INPUT
[1] Add a new student
[2] Add multiple students
[3] Add a new course
[4] Change mark for a student

    LIST
[5] List all courses
[6] List all students
[7] View/Update an existing course
[8] Sort student by GPA descending
    """)
        try:
            select = int(input("Enter your choice: "))
        except ValueError:
            select = -1
        match select:
            case 0:
                return s_list, c_list, m_list
            case 1:
                s_list, m_list = add_student(stdscr, s_list, c_list, m_list)
            case 2:
                s_list, m_list = add_n_student(stdscr, s_list, c_list, m_list)
            case 3:
                c_list, m_list = add_course(stdscr, s_list, c_list, m_list)
            case 4:
                c_select = print_list_get_element(stdscr, c_list, 1, True)
                if c_select == 0:
                    return c_list
                c_index = c_select - 1

                m_list = update_mark(stdscr, s_list, c_list, c_index, m_list)
            case 5:
                print_list_get_element(stdscr, c_list, 1, False)
            case 6:
                print_list_get_element(stdscr, s_list, 0, False)
            case 7:
                c_list, m_list = view_update_course(stdscr, s_list, c_list, m_list)
            case 8:
                obj = Student()
                obj.get_list_gpa_desc(stdscr, s_list, c_list, m_list)
            case _:
                print("Invalid option!")


class Student:
    __list_sid: list = []
    __default_sid: str = ""
    __default_sname: str = "student_name"
    __default_sdob: date = date(1, 1, 1)
    __default_smark: list = []
    __default_gpa: float = math.floor(0 * 10) / 10

    def __init__(self):
        self.__sid: str = self.__default_sid
        self.__sname: str = self.__default_sname
        self.__sdob: date = self.__default_sdob
        self.__smark: list = self.__default_smark
        self.__gpa: float = self.__default_gpa

    # getters
    def get_list_sid(self, stdscr):
        if len(self.__list_sid) == 0:
            # print("No student id used yet!")
            stdscr.addstr(14, 0, "No student id used yet!", curses.color_pair(1))
            return
        # print("Used student ids: " + str(self.__list_sid))
        stdscr.addstr(14, 0, "Used student ids: ", curses.color_pair(2))
        for i in range(len(self.__list_sid)):
            if i < 10:
                stdscr.addstr(15 + i, 0, self.__list_sid[i])
            else:
                stdscr.addstr(15 + i - 10, 25, self.__list_sid[i])
        stdscr.refresh()

    def get_list_gpa_desc(self, stdscr, s_list, c_list, m_list):
        print("    Student list sorted by GPA descending:")
        list_gpa = []
        if len(self.__list_sid) == 0:
            print("No student added yet!")
            return list_gpa
        s_array = np.array(s_list, dtype=object)
        sorted_index = np.argsort([-s.get_gpa(c_list, m_list) for s in s_array])
        sorted_s_list = s_array[sorted_index]
        for s in sorted_s_list:
            print(f"{s.get_sname()} (ID: {s.get_sid()}): {s.get_gpa(c_list, m_list)}")

    def get_sid(self):
        return self.__sid

    def get_sname(self):
        return self.__sname

    def get_sdob(self):
        return self.__sdob

    def get_gpa(self, c_list, m_list):
        self.update_gpa(c_list, m_list)
        return self.__gpa

    # setters
    def append_list_sid(self, sid):
        self.__list_sid.append(sid)

    def remove_list_sid(self, sid):
        self.__list_sid.remove(sid)

    def delete_list_sid(self):
        self.__list_sid.clear()

    def set_sid(self, stdscr, y):
        while True:
            try:
                # blank
                for i in range(50):
                    for j in range(y, 14):
                        stdscr.addstr(j, i, " ")
                self.get_list_sid(stdscr)
                stdscr.addstr(y, 0, "Enter student id: ")
                stdscr.refresh()
                sid = ask_sid(y)
                if not sid:
                    stdscr.addstr(y+1, 0, "Student id cannot be blank!", curses.color_pair(1))
                    raise ValueError
                if sid in self.__list_sid:
                    stdscr.addstr(y+1, 0, "ID existed, try another one!", curses.color_pair(1))
                    raise ValueError
                self.append_list_sid(sid)
                break
            except ValueError:
                pass
        self.__sid = sid

    def set_sname(self, stdscr, y):
        # blank
        for i in range(50):
            for j in range(y+1, y+2):
                stdscr.addstr(j, i, " ")

        stdscr.addstr(y+1, 0, "Enter student name: ")
        stdscr.refresh()
        sname = ask_sname(y+1)
        if not sname:
            sname = self.__default_sname
            stdscr.addstr(y+1, 20, self.__default_sname)
            stdscr.refresh()
        self.__sname = sname

    def set_sdob(self, stdscr, y):
        while True:
            try:
                # blank
                for i in range(50):
                    for j in range(y+2, y+6):
                        stdscr.addstr(j, i, " ")
                stdscr.refresh()

                stdscr.addstr(y+2, 0, "Enter student birthday: ")
                stdscr.addstr(y+3, 4, "Year: ")
                stdscr.addstr(y+4, 4, "Month: ")
                stdscr.addstr(y+5, 4, "Day: ")
                stdscr.refresh()
                year, month, day = ask_ymd(y+3)
                if not year and not month and not day:
                    sdob = self.__default_sdob
                    break
                sdob = date(int(year), int(month), int(day))
                break
            except ValueError as ve:
                # blank
                for i in range(50):
                    for j in range(y + 6, y + 8):
                        stdscr.addstr(j, i, " ")
                stdscr.refresh()
                stdscr.addstr(y+6, 0, f"Invalid input: {ve}!", curses.color_pair(1))
                stdscr.refresh()
        self.__sdob = sdob

    def update_smark(self, c_list, m_list):
        """reset and get sorted mark of each course according to c_list (or list_cid)"""
        self.__smark.clear()
        list_cid = [c.get_cid() for c in c_list]
        # get mark obj of student
        s_mark = [m for m in m_list if m.get_msid() == self.__sid]
        for cid in list_cid:
            self.__smark.append(
                next(m.get_mval() for m in s_mark if m.get_mcid() == cid)
            )

    def update_gpa(self, c_list, m_list):
        """reset and calc new gpa based on new smark"""
        self.update_smark(c_list, m_list)

        numpy_smark = np.array([
            mval for mval in self.__smark
        ])
        numpy_cre = np.array([
            c.get_cre() for c in c_list
        ])
        obj = Course()
        sum_cre = obj.get_sum_cre(c_list)
        if sum_cre != 0:
            self.__gpa = math.floor(np.sum(numpy_smark * numpy_cre) / sum_cre * 10) / 10


def ask_sid(y):
    win = curses.newwin(1, 11, y, 18)
    box = Textbox(win)
    curses.curs_set(1)
    box.edit()
    curses.curs_set(0)
    sid = box.gather()
    return sid


def ask_sname(y):
    win = curses.newwin(1, 11, y, 20)
    box = Textbox(win)
    curses.curs_set(1)
    box.edit()
    curses.curs_set(0)
    sname = box.gather()
    return sname


def ask_ymd(y):
    win = curses.newwin(1, 5, y, 10)
    box = Textbox(win)
    curses.curs_set(1)
    box.edit()
    curses.curs_set(0)
    year = box.gather()

    win = curses.newwin(1, 3, y+1, 11)
    box = Textbox(win)
    curses.curs_set(1)
    box.edit()
    curses.curs_set(0)
    month = box.gather()

    win = curses.newwin(1, 3, y+2, 9)
    box = Textbox(win)
    curses.curs_set(1)
    box.edit()
    curses.curs_set(0)
    day = box.gather()
    return year, month, day


class Course:
    __list_cid: list = []
    __sum_cre: int = 0
    __default_cid: str = ""
    __default_cname: str = "course_name"
    __default_cre: int = 0

    def __init__(self):
        self.__cid = self.__default_cid
        self.__cname = self.__default_cname
        self.__cre = self.__default_cre

    # getters
    def get_list_cid(self, stdscr):
        if len(self.__list_cid) == 0:
            print("No course id used yet!")
            return
        print("Used course ids: " + str(self.__list_cid))

    def get_sum_cre(self, c_list):
        self.__sum_cre: int = 0
        for c in c_list:
            self.__sum_cre += c.get_cre()
        return self.__sum_cre

    def get_cid(self):
        return self.__cid

    def get_cname(self):
        return self.__cname

    def get_cre(self):
        return self.__cre

    # setters
    def append_list_cid(self, cid):
        self.__list_cid.append(cid)

    def remove_list_cid(self, cid):
        self.__list_cid.remove(cid)

    def set_cid(self, stdscr):
        while True:
            try:
                self.get_list_cid(stdscr)
                cid = input("Enter course id: ")
                if not cid:
                    print("\nCourse id cannot be blank!")
                    raise ValueError
                if cid in self.__list_cid:
                    print(f"\nID existed, try another one!")
                    raise ValueError
                self.append_list_cid(cid)
                break
            except ValueError:
                pass
        self.__cid = cid

    def set_cname(self, stdscr):
        cname = input("Enter course name: ")
        if not cname:
            cname = self.__default_cname
        self.__cname = cname

    def set_cre(self, stdscr):
        while True:
            try:
                cre = input("Enter credit value: ")
                if not cre:
                    cre = self.__default_cre
                cre = int(cre)
                break
            except ValueError:
                print(f"\nInvalid input!")
        self.__cre = cre


class Mark:
    """Store locally in each student"""
    __default_mval: float = math.floor(0 * 10) / 10

    def __init__(self, msid, mcid):
        self.__msid = msid
        self.__mcid = mcid
        self.__mval = self.__default_mval

    # getters
    def get_msid(self):
        return self.__msid

    def get_mcid(self):
        return self.__mcid

    def get_mval(self):
        return self.__mval

    # setters
    def set_mval(self, stdscr):
        while True:
            try:
                mval = input("Enter new mark (scale 20): ")
                if not mval:
                    self.__mval = self.__default_mval
                    break
                mval = float(mval)
            except ValueError:
                mval = -1
            if 0 <= mval <= 20:
                self.__mval = math.floor(mval * 10) / 10
                break
            else:
                print("Invalid option!\n")


def main(stdscr):
    curses.use_default_colors()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)

    test_screen(stdscr)

    # init
    s_list = []
    c_list = []
    m_list = []

    s_list, c_list, m_list = home(stdscr, s_list, c_list, m_list)


if __name__ == "__main__":
    try:
        wrapper(main)
    except KeyboardInterrupt:
        print("\033[91m" + "\n\nForced to exit using keyboard!" + "\033[0m")
    except EOFError as e:
        print(e)
