# This script shows different ways to convert a 9 characters string in a
# nested list which can be read like a matrix using two indexes for rows
# and columns. The bruteforce is commented because is basically garbage,
# it's better to do it with enumerate() built-in method/function.

cells = "abcdefghijklmnop"
width = 4


def check_square_array(c_s, w):
    """c_s -> cells string
       w   -> width"""
    if len(c_s) / w != w:
        print("Cannot create square array")
        exit()


check_square_array(cells, width)


############################
# Made by bruteforce:
#
def bruteforce(c_s, w):
    """c_s -> cells string
       c   -> single cell
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


explicit_for_wo_enumerate(cells, width)
nested_list_comprehension(cells, width)
