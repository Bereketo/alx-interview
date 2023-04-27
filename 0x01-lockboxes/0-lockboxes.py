#!/usr/bin/env python3
"""solves the lockbox problem """


def canUnlockAll(boxes):
    # Create a set to keep track of the opened boxes
    opened_boxes = set([0])
    # Create a queue to keep track of the keys that need to be tried next
    queue = boxes[0]
    # While there are still keys to be tried
    while queue:
        # Pop a key from the queue
        key = queue.pop(0)
        # If the corresponding box is not already opened,
        # open it and add its keys to the queue
        if key not in opened_boxes and key < len(boxes):
            opened_boxes.add(key)
            queue.extend(boxes[key])
    # Check if all the boxes have been opened
    return len(opened_boxes) == len(boxes)
