#!/usr/bin/python3
""" lockboxes."""


def canUnlockAll(boxes):
    """ Function that checks if all boxes can be opened."""
    my_boxes = set()

    def dfs(current_box):
        my_boxes.add(current_box)

        for key in boxes[current_box]:
            if key not in my_boxes:
                dfs(key)
    dfs(0)

    return len(my_boxes) == len(boxes)