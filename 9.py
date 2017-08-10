# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import itertools as it

a = [x for x in range(501)]

candidates = list(it.product(a, repeat=2))

for x in candidates:
    c_squared = (x[0] ** 2) + (x[1] ** 2)
    c = c_squared ** (1/2)
    if x[0] < x[1] < c:
        if x[0] + x[1] + c == 1000:
            print(x[0], x[1], c, x[0] * x[1] * c)
            break

# smallest:  1,   2,   3
# largest:   1, 499, 500
