#!/usr/bin/python3

from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')

print('Initial queue')
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())

print(q)
