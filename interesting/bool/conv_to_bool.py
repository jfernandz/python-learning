# X or Y  --> Y is evaluated only if X is False
# X and Y --> Y is evaluated only if X is True

# So we need in the if that `a and a[0] < b[0]` just be evaluated only
# when `not b` is False, i.e. `b` list is not empty. Because if `b` list
# is empty, b[0] will give an IndexError

def merge_arrays(a, b):
    # "c" will contain the result of merging arrays "a" and "b"
    c = []
    while a or b:
        if not b or a and a[0] < b[0]:
            # removing the first element from "a" and adding it to "c"
            c.append(a[0])
            a.pop(0)
        else:
            # removing the first element from "b" and adding it to "c"
            c.append(b[0])
            b.pop(0)
    print()
    print(c)


a = [1, 2, 3, 5, 6]
b = [2, 3, 4, 4]


merge_arrays(a, b)
