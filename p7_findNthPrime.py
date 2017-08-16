# Project Euler problem at https://projecteuler.net/problem=7

def findNthPrime(a):

    primes = [2]
    checking = 2
    running = 'True'

    while running == 'True':
        length = len(primes)
        if length == a:
            running = 'False'
        else:
            checking += 1
            for i, x in enumerate(primes):
                if i == length - 1:
                    if checking % x == 0:
                        break
                    else:
                        primes.append(checking)
                elif checking % x == 0:
                    break

    print(primes[-1])

a = int(input('Which prime? '))
findNthPrime(a)
