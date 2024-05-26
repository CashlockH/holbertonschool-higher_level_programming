#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if not my_list:
            return 0
        for i, j in enumerate(my_list):
            if i < x:
                print("{}".format(j), end="")
            else:
                break
        print()
        if i < x:
            return i + 1
        return i
    except Exception as err:
        print("this is not valid")
