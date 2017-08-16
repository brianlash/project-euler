# Project Euler problem at https://projecteuler.net/problem=10

def findNthPrime(a):

    primes = [2]
    checking = 1
    running = 'True'

    while running == 'True':
        length = len(primes)
        if checking >= a:
            running = 'False'
        else:
            checking += 2
            for i, x in enumerate(primes):
                if i == length - 1:
                    if checking % x == 0:
                        break
                    else:
                        primes.append(checking)
                elif checking % x == 0:
                    break

    print(sum(primes))

a = int(input('Which prime? '))
findNthPrime(a)
