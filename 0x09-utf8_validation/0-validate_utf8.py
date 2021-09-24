#!/usr/bin/python3
"""
Determines if a given data set represents a
 valid UTF-8 encoding.
"""


def validUTF8(data):
    "iterate over data and check if utf-8"
    for i in data:
        if int(bin(i)[2:8]) > 111110:
            return False
    return True
