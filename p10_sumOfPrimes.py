# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


# NOTE: This is a brute force solution that treats every odd
# number as a potential prime candidate. It finds a solution,
# however it is computationally expensive and requires >10 min
# on a 2.7GHz machine. There are faster methods.

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

a = 2000000
findNthPrime(a)
