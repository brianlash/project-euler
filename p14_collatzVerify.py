# Project Euler problem at https://projecteuler.net/problem=14

import time

x = 837799
paths = 1

print(paths, ': ', int(x))

while x != 1:
    if x % 2 == 0:
        x = x / 2
        paths += 1
        print(paths, ': ', int(x))
        time.sleep(0.1)
    else:
        x = (3 * x) + 1
        paths += 1
        print(paths, ': ', int(x))
        time.sleep(0.1)
