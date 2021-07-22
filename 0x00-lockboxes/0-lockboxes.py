#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes
can be opened.
"""


def canUnlockAll(boxes):
    """Return true if all boxes can be opened or false if not"""
    new = [0]
    for i in new:
        for n in boxes[i]:
            if n not in new:
                new += [n]
    if len(new) == len(boxes):
        return True
    return False
