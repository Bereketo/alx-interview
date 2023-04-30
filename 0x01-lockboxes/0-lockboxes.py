#!/usr/bin/env python3
"""sloves the lockboxes problem:
        determines if all boxes can be unlocked
        A key with the same number as a box opens it & box[0] is unlocked
"""


def canUnlockAll(boxes):
    """ Arguments:
            boxes: list of lists
       Returns:
            True: if all boxes can be unlocked
            False: if all boxes can't be unlocked
    """
    n = len(boxes)
    unlockedBoxes = set([0])
    boxesToTry = set([0])
    while len(boxesToTry) > 0:
        box = boxesToTry.pop()
        for key in boxes[box]:
            if key < n and key not in unlockedBoxes:
                unlockedBoxes.add(key)
                boxesToTry.add(key)
    return n == len(unlockedBoxes)
