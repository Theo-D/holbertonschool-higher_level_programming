#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for elm in my_list[:x]:
        try:
            print("{}".format(elm), end="")
            count += 1
        except IndexError:
            print("Index Error")
            break
    print()
    return count
