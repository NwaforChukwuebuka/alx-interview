# alx-interview-
ALX_INTERVIEW





2. Unlocking All Boxes
Description

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to other boxes. The task is to write a method that determines if all the boxes can be opened.

Prototype

def canUnlockAll(boxes)

boxes: A list of lists. Each inner list represents a box and contains keys (positive integers) to other boxes.

Requirements

    A key with the same number as a box opens that box.
    All keys will be positive integers.
    There can be keys that do not have corresponding boxes.
    The first box boxes[0] is initially unlocked.
    The method should return True if all boxes can be opened, else return False.

Examples:


#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False

