#!/usr/bin/python3

from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    queue = deque([0])

    while queue:
        box = queue.popleft()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if key not in visited:
                    queue.append(key)

    return len(visited) == n

