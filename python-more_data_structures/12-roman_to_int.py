#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    num = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    romanDict = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for letter in roman_string:
        if letter in romanDict.keys():
            for pair in romanDict:
                if letter == pair:
                    if romanDict[letter] > num:
                        res -= num
                        num = romanDict[letter] - num
                    else:
                        num = romanDict[letter]
                    res += num
        else:
            return 0
    return res
