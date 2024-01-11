#!/usr/bin/python
""" opening lockboxes """

def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False

    # Initialize a set to keep track of opened boxes
    opened_boxes = {0}

    # Initialize a stack to perform depth-first search
    stack = [0]

    while stack:
        current_box = stack.pop()

        # Check keys in the current box
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                stack.append(key)

    # Check if all boxes can be opened
    return len(opened_boxes) == len(boxes)
