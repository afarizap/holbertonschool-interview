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
    new = set(boxes[0])
    unlocked = 1
    while unlocked < len(boxes) - 1:
        print(unlocked, boxes, new)
        tmp = new.copy()
        if len(new) == 0:
            return False
        for i in tmp:
            if len(boxes[i]) == 0:
                new.discard(i)
            else: 
                new |= set(boxes[i])
                boxes[i] = []
                new.discard(i)
                unlocked += 1
    return True
