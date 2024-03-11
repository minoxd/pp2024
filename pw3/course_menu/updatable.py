def updatable(s_list, c_mark, mode):
    msid_set = set(m.get_msid() for m in c_mark)
    update = [s for s in s_list if s.get_sid() in msid_set]
    match mode:
        case 0:
            for u in update:
                who = next(m for m in c_mark if m.get_msid() == u.get_sid())
                print(f"{u.get_sname()} (ID: {u.get_sid()}): {who.get_mval()}")
        case 1:
            while True:
                print("[0] Exit")
                for i in range(len(update)):
                    who = next(m for m in c_mark if m.get_msid() == update[i].get_sid())
                    print(f"[{i + 1}] {update[i].get_sname()} (ID: {update[i].get_sid()}): {who.get_mval()}")
                try:
                    s_select = int(input("Enter your choice: "))
                except ValueError:
                    s_select = -1
                if 0 <= s_select <= len(update):
                    s_index = s_select - 1
                    if s_index == -1:
                        return -1
                    # return selected student's id
                    return update[s_index].get_sid()
                else:
                    print("Invalid option!\n")
        case 2:
            pass


