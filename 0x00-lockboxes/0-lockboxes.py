#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes
can be opened.
"""


def canUnlockAll(boxes):
    """ returns true if all boxes can be open """
    new_list = [0]
    
    for index in new_list:
        for num in boxes[index]:
            if num not in new_list and num < len(boxes) \
               and isinstance(num, int) and num >= 0:
                new_list.append(num)

    return(bool(len(new_list) == len(boxes)))
