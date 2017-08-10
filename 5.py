# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

numbers = [x for x in range(1, 21)]
candidate = 0
running = 'True'

while running == 'True':
    candidate += 2
    for x in numbers:
        if x == 20:
            if candidate % x == 0:
                running = 'False'
        elif candidate % x != 0:
            break

print(candidate)
