# Project Euler problem at https://projecteuler.net/problem=25
#
fibonacci = [1, 1]

for x in range(1,10001):
    fibonacci.append(fibonacci[x-1] + fibonacci[x])
    if len(str(fibonacci[-1])) == 1000:
        # We seeded the sequence with 2 digits, so add 2 to the index
        print(x+2)
        break
