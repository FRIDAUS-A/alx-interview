#!/usr/bin/python3
"""
Implement using graph and a deep search algorithm
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you. Each box is
    numbered sequentially from
    0 to n - 1 and each box may contain keys to the other boxes.
    """
    opened = set()

    stack = [0]
    while len(stack) > 0:
        current = stack.pop()  # get current stack
        opened.add(current)  # add current to the new set
        for key in boxes[current]:
            # to avoid infinite loop, check if key in opened or in stack
            if key in opened or key in stack or key > len(boxes) - 1:
                continue  # skip and go to the next one
            stack.append(key)
            if len(stack) == len(boxes) - 1:
                return True
    return len(opened) == len(boxes)
