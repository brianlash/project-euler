# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def findNthPrime(a):

    primes = [2]
    checking = 1
    running = 'True'

    while running == 'True':
        length = len(primes)
        print(length, primes[-1])
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
