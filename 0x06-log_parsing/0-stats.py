#!/usr/bin/python3
""" reads stdin line by line and computes metrics """
import sys


calls = 0
size = 0
stats = {}

try:
    for line in sys.stdin:
        n = line.split()
        calls += 1
        size += int(n[8])
        if n[7] in stats.keys():
            tmp = int(stats[n[7]]) + 1
            stats.update({n[7]: tmp})
        else:
            stats.update({n[7]: 1})
        if calls % 10 == 0:
            print("File size: {}".format(size))
            for k, v in sorted(stats.items()):
                print("{}: {}".format(k, v))
except KeyboardInterrupt:
    sys.stdout.flush()
finally:
    print("File size: {}".format(size))
    for k, v in sorted(stats.items()):
        print("{}: {}".format(k, v))
