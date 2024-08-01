#!/usr/bin/python3
from collections import deque

""" Checks if a box containing boxes (list of lists) can be unlocked 
    using the keys in each sub boxes
"""


def canUnlockAll (boxes):
    """ Checks if the sub-boxess can ALL be unlocked """

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    queue = deque([0])


    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)


    return all(unlocked)


