#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    newStr = ''
    for char in str:
        if i != n:
            newStr += char
        i = i + 1
    return newStr
