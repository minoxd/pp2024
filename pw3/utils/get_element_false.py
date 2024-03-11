def get_element_false(the_list, mode, label1, func1):
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


