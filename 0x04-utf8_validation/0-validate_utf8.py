#!/usr/bin/python3
"""check if data is utf-8 valid """
import codecs


def validUTF8(data):
    """A method that determines if
        a given data set represents a valid UTF-8 encoding.
    """
    try:
        bytes_data = bytes(data)
        codecs.decode(bytes_data, 'utf-8')
        return True
    except (UnicodeDecodeError, ValueError):
        return False
