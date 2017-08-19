# Project Euler problem at https://projecteuler.net/problem=23
#
# Step 1: Find all abundant numbers
from functools import reduce
from itertools import permutations

def factors(n):
    return list(set(sorted(reduce(list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))[:-1]))

abundant_numbers = []

for x in range(1,28124):
    temp = factors(x)
    if x < sum(temp):
        abundant_numbers.append(x)

# Get the distance to each sequential abundant number, Ex. 12: 6 because the
# next abundant number above 12 is 18. This is useful for the iterative
# mapping that follows
abundant_distance = {}

for x in range(len(abundant_numbers)):
    abundant_distance[abundant_numbers[x]] = abundant_numbers[x] - \
        abundant_numbers[x-1]

abundant_distance.pop('12', None)

# Create the starter abundant sum list
# This adds 12 (the first abundant number) to all other abundant numbers
abundant_sums = []

starter_list = []

for x in abundant_numbers:
    starter_list.append(abundant_numbers[0] + x)

abundant_sums.append(starter_list)

for z in abundant_numbers[1:]:
    starter_list = list(map(lambda x: x + abundant_distance[z], starter_list))
    abundant_sums.append(starter_list)

flat_abundant_sums = list(set([y for x in abundant_sums for y in x]))

nonabundant_sums = []

for x in range(1,28124):
    if flat_abundant_sums.count(x) >= 1:
        pass
    else:
        nonabundant_sums.append(x)

print(sum(nonabundant_sums))
