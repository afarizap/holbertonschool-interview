#!/usr/bin/python3
"""
Determines if a given data set represents a
 valid UTF-8 encoding.
"""


def validUTF8(data):
    "iterate over data and check if utf-8"
    for i in data:
        try:
            if int(i) == 0:
                return False
            if int(i) > 126:
                return False
        except:
            return False
    return True
