# Project Euler problem at https://projecteuler.net/problem=22
#
names = open('p022_names.txt', 'r')
names_read = names.read() # read the file in

names_split = names_read.split('","') # split the file on ','

names_split[0] = names_split[0][1:] # fix the first entry
names_split[-1] = names_split[-1][:6] # and the last

names_alphabetized = sorted(names_split) # put in alphabetical order

names_dict = {}

for i, x in enumerate(names_alphabetized):
    temp = 0
    for y in x:
        temp += ord(y) - 64
    names_dict[x] = (i+1) * temp # need to use i + 1 because of 0 index

print(sum(names_dict.values()))

names.close()
