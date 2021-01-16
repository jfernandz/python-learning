#!/usr/bin/env python

# This code explains the equivalence between
# different ways to unpack a nested list

pairs = [[1, 2], [3, 4]]

flattened_list_1 = []
for column in zip(*pairs):               # A
    for string in column:                # B
        flattened_list_1.append(string)  # C

flattened_list_2 = [string for column in zip(*pairs) for string in column]

# exact same thing as flattened_list_2,
# just split into lines for explanation
flattened_list_3 = [
    string                               # C
    for column in zip(*pairs)            # A
    for string in column                 # B
]

print(flattened_list_1)
print(flattened_list_1 == flattened_list_2 == flattened_list_3)

# You can use also from_itertable() method from chain class
# in the itertools module

from itertools import chain

print(list(chain.from_iterable(pairs)))

# or with star expression
print(list(chain(*pairs)))
