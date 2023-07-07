#!/usr/bin/python3
"""
0. Lockboxes
"""


def canUnlockAll(boxes):
    """Write a method that determines if all the boxes can be opened"""
    if len(boxes) <= 1:
        return True

    req_keys = set(range(1, len(boxes)))
    avail_keys = set()

    for idx, box in enumerate(boxes):
        curr_req_keys = req_keys.copy()
        if idx > 0:
            curr_req_keys.remove(idx)
        for p_key in box:
            if p_key in curr_req_keys:
                avail_keys.add(p_key)

    return req_keys == avail_keys
