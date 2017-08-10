# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

import itertools as it

list_1 = [x for x in range(100, 1000)]

new_list = list(it.product(list_1, repeat=2))

max_product = 0

for x in new_list:
    # The first of the tuple pair multipled by the second
    temp = x[0] * x[1]
    # If the product is a palindrome...
    if temp == int(str(temp)[::-1]):
        if temp > max_product:
            max_pair = x
            max_product = temp

print(max_pair, max_product)
