#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x >= len(my_list):
            x = len(my_list)
        for i, j in enumerate(my_list):
            if i < x - 1:
                print("{}".format(j), end = "")
            else:
                break
        print("{}".format(j))
        return x
    except:
        pass
