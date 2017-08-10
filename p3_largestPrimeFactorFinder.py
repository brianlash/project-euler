# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

current_candidate = 600851475143

def nextFactor(candidate):
    checking = 2

    while checking < candidate:
        if candidate % checking == 0:
            return candidate / checking
        checking += 1

    return 'Done'

while True:
    new_candidate = nextFactor(current_candidate)
    if new_candidate == 'Done':
        print(current_candidate)
        break
    else:
        current_candidate = new_candidate

# checknum = 600851475143
