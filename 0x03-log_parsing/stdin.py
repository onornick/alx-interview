#!/usr/bin/python3
import sys

with open('file.txt', 'a') as f:
    for line in sys.stdin:
        f.write(line)
    f.close()



