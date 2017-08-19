# Project Euler problem at https://projecteuler.net/problem=24
#
import itertools as it

x = [x for x in range(10)]

number = list((sorted(list(it.permutations(x)))[999999]))

millionth_lexicographic = ''

for x in number:
    millionth_lexicographic += str(x)

print(millionth_lexicographic)

#print(int(millionth_lexicographic))
