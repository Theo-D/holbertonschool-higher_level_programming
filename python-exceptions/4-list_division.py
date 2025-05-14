#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for elm1, elm2 in zip(my_list_1[:list_length], my_list_2[:list_length]):
        res = 0
        try:
            res = elm1 / elm2
        except TypeError:
            print("wrong type")
            pass
        except ZeroDivisionError:
            print("division by 0")
            pass
        except IndexError:
            print("out of range")
            pass
        finally:
            newList.append(res)
    return newList
