#!/usr/bin/python3
"""
Determines if a given data set represents a
 valid UTF-8 encoding.
"""


def validUTF8(data):
    "iterate over data and check if utf-8"
    for i in data:
        if bin(i)[:9] >= bin(126):
            print(bin(i)[:9])
            return False
    return True
