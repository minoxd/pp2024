def addable(s_list, c_mark, mode):
    msid_set = set(m.get_msid() for m in c_mark)
    add = [s for s in s_list if s.get_sid() not in msid_set]
    match mode:
        case 0:
            for a in add:
                print(f"{a.get_sname()} (ID: {a.get_sid()}): n/a")
        case 1:
            while True:
                print("[0] Exit")
                for i in range(len(add)):
                    print(f"[{i + 1}] {add[i].get_sname()} (ID: {add[i].get_sid()}): n/a")
                try:
                    s_select = int(input("Enter your choice: "))
                except ValueError:
                    s_select = -1
                if 0 <= s_select <= len(add):
                    s_index = s_select - 1
                    if s_index == -1:
                        return -1
                    # return selected student's id
                    return add[s_index].get_sid()
                else:
                    print("Invalid option!\n")


