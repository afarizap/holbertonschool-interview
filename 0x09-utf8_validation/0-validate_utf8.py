#!/usr/bin/python3
"""
Determines if a given data set represents a
 valid UTF-8 encoding.
"""
import chardet

def validUTF8(data):
    return max(data) < 128