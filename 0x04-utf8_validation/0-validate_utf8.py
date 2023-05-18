#!/usr/bin/python3
"""Check UTF-8 valid
"""


def validUTF8(data):
    """a method to determine if a data is utf-8 valid
    """
    remaining_bytes = 0

    for byte in data:
        if remaining_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                remaining_bytes -= 1
            else:
                return False

    return remaining_bytes == 0
