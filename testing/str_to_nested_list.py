# This script shows different ways to convert a string of characters in a
# nested list which can be read like a matrix using two indexes for rows
# and columns.
#
# The bruteforce function is the clearest way but basically garbage.
# I think explicit_for_wo_enumerate() and nested_list_comprehension()
# the best ways to do this


############################
# Made by bruteforce:
#
def bruteforce(c_s, w):
    """c_s -> cells string
       w   -> width
       m   -> final array (matrix)"""
    m = []
    k = 0
    for i in range(w):
        m.append([])
        for j in range(w):
            # print(c_s[k])
            m[i].append(c_s[k])
            k += 1

    print(m)


############################
# Explicit for loop with enumerate (for debug purposes):
#
def explicit_for_w_enumerate(c_s, w):
    """c_s -> cells string
       c   -> single cell
       w   -> array width
       m   -> final array"""
    m = []
    for i in range(w):
        m.append([])
        for j, c in enumerate(c_s[i*w:(i+1)*w]):
            # Debug prints
            print(f"Slice indexes: cells[{i*w}:{(i+1)*w}]")
            print(list(enumerate(c_s[i*w:(i+1)*w])))
            print("Enum indexes and cell:", f"({j}, '{str(c)}')")
            print("\n")
            ##############
            m[i].append(c)

    print("\nWith enumerate():")
    print(m)


############################
# Explicit for loop without enumerate:
#
def explicit_for_wo_enumerate(c_s, w):
    """c_s -> cells string
       c   -> single cell
       w   -> array width
       m   -> final array"""
    m = []
    for i in range(w):
        m.append([])
        for c in c_s[i*w:(i+1)*w]:
            m[i].append(c)

    print("\nWithout enumerate():")
    print(m)


############################
# Nested list comprehension:
#
def nested_list_comprehension(c_s, w):
    """c_s -> cells string
       c   -> single cell
       w   -> array width"""
    print("\nNested list comprehension:")
    print([[c for c in c_s[i*width:(i+1)*w]] for i in range(w)])


############################
# Main function to check if posible build an
# square array
#
def check_if_square_and_do(c_s, w):
    """c_s -> cells string
       w   -> width"""
    if len(c_s) / w != w:
        print("Cannot create square array")
        exit()
    else:
        explicit_for_wo_enumerate(c_s, w)
        nested_list_comprehension(c_s, w)


cells = "abcdefghijklmnop"
width = 4

check_if_square_and_do(cells, width)
