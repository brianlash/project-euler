# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?

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

a = 10001
findNthPrime(a)
