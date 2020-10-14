# Align (padding) strings and integers is possible using format specifications
# further info can be found in

# https://docs.python.org/3/library/string.html#format-specification-mini-language

# However, we will play here with this concepts, for example, I want a string
# with ten digits, but zeroes in the first 3:


import random

# Number of zeroes what we want to place at left
zeroes = 8

# We first generate a random integer between 0 and 10000000000
n = random.randrange(0, 10000000000)
# Also we must fill with zeroes in the case the random integer
# generated is not 10 digits long
n = f'{n:0>10}'

# Then we check if the first `zeroes` digits are zeroes (we are
# using a variable to make the program more versatile)
while n[:zeroes] != '0'*zeroes:
    # If they aren't, we generate a new string and fill it at left with
    # zeroes again
    n = str(random.randrange(0, 10000000000))
    n = f'{n:0>10}'
else:
    # Once these first digits are zeroes we can print the string and
    # exit from the loop
    print(n)
