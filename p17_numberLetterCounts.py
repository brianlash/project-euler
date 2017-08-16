# Project Euler problem at https://projecteuler.net/problem=17

tens_lookup = {
    #1: 10,# don't need this because 10 is included in one_to_ninety_nine
    2: 6,# twenty
    3: 6,# thirty
    4: 5,# forty
    5: 5,# fifty
    6: 5,# sixty
    7: 7,# seventy
    8: 6,# eighty
    9: 6# ninety
}

hundreds_lookup = {
    1: 10,# one hundred
    2: 10,# two hundred
    3: 12,# three hundred
    4: 11,# four hundred
    5: 11,# five hundred
    6: 10,# six hundred
    7: 12,# seven hundred
    8: 12,# eight hundred
    9: 11,# nine hundred
}

ones_and_tens = {
    1: 3,# one
    2: 3,# two
    3: 5,# three
    4: 4,# four
    5: 4,# five
    6: 3,# six
    7: 5,# seven
    8: 5,# eight
    9: 4,# nine
    10: 3,# ten
    11: 6,# eleven
    12: 6,# twelve
    13: 8,# thirteen
    14: 8,# fourteen
    15: 7,# fifteen
    16: 7,# sixteen
    17: 9,# seventeen
    18: 8,# eighteen
    19: 8,# nineteen
}

hundreds = {}

# finish building ones_and_tens
for x in range(20, 100):
    if x % 10 == 0:
        ones_and_tens[x] = tens_lookup[int(x/10)]
    else:
        ones_and_tens[x] = tens_lookup[int(x/10)] + ones_and_tens[x % 10]

# enter hundreds
for x in range(100, 1000):
    if x % 100 == 0:
        hundreds[x] = hundreds_lookup[int(x/100)]
    else:
        # add 3 for letters in "and"
        hundreds[x] = hundreds_lookup[int(x/100)] + ones_and_tens[x % 100] + 3

# merge the dictionaries
one_to_one_thousand = {**ones_and_tens, **hundreds}

# add 1000
one_to_one_thousand[1000] = 11

print(sum(one_to_one_thousand.values()))
