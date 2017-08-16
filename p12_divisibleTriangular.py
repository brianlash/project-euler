# Project Euler problem at https://projecteuler.net/problem=12

from functools import reduce

# Quickly identify factors
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

triangles = [1]
current = 1

while True:
    current += 1
    triangles.append(triangles[-1] + current)
    if len(factors(triangles[-1])) > 500:
        print(triangles[-1])
        break
