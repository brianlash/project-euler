# Project Euler problem at https://projecteuler.net/problem=20

factorial = 100

for x in reversed(range(1,factorial)):
    factorial *= x

new = list(''.join(str(factorial)))

factorial_sum = 0

for x in new:
    factorial_sum += int(x)

print(factorial_sum)
