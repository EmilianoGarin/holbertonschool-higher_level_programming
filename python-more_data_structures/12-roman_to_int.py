#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return (None)
    ret = 0
    ara_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for old_l, l in zip(' ' + roman_string, roman_string):
        if l in ara_rom:
            if old_l in ara_rom and ara_rom[l] > ara_rom[old_l]:
                ret += -ara_rom[old_l] * 2
            ret += ara_rom[l]
    return (ret)
