# Project Euler problem at https://projecteuler.net/problem=21
#
from functools import reduce

# Quickly identify factors
def factors(n):
    return sorted(reduce(list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))[:-1]

factor_dict = {}

for x in range(1,10001):
    factor_list = factors(x)
    factor_sum = sum(factor_list)
    factor_dict[x] = factor_sum

amicable_list = []

for key, value in factor_dict.items():
    if key == value:
        pass
    else:
        if factor_dict.get(value) == key:
            if key in amicable_list:
                pass
            else:
                amicable_list.append(key)
                amicable_list.append(value)

print(sum(amicable_list))
