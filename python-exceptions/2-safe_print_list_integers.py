#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for elm in my_list[:x]:
            try:
                print("{:d}".format(elm), end="")
                i += 1
            except ValueError:
                pass
    except IndexError:
        return
    print()
    return i
