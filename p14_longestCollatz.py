# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# Note: Once the chain starts the terms are allowed to go above one million.


# NOTE: The following code executes in < 1 min. It could be improved by taking
# advantage of the repetition in Collatz.
# Ex: 16 will always proceed 16 => 8 => 4 => 2 => 1.

sequence, longest_sequence, number = 0, 0, 0

for x in range(1, 1000000):
    y = x
    if y % 1000 == 0:
        print(y)
    while y != 1:
        if y % 2 == 0:
            y = y / 2
            sequence += 1
        else:
            y = (3 * y) + 1
            sequence += 1
    sequence += 1
    if sequence > longest_sequence:
        number = x
        longest_sequence = sequence
    sequence = 0

print(number, longest_sequence)

# A: 837799
