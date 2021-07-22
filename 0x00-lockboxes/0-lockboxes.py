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
    old = [0]
    boxes[0] = []
    unlocked = 1
    while unlocked < len(boxes):
        print(unlocked, boxes, new, len(boxes), old)
        tmp = new.copy()
        if len(new) == 0:
            return False
        for i in tmp:
            new |= set(boxes[i])
            boxes[i] = []
            new.discard(i)
            if i not in old:
                unlocked += 1
                old += [i]
        # print(unlocked, boxes, new, len(boxes))
    return True
