#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return (0)
    ret = 0
    rom_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for old_l, l in zip(' ' + roman_string, roman_string):
        if l in rom_int:
            if old_l in rom_int and rom_int[l] > rom_int[old_l]:
                ret += -rom_int[old_l] * 2
            ret += rom_int[l]
        else:
            return (0)
    return (ret)
