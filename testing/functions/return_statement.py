def print_smt():
    print("hello")
    return 1


print_smt()
print(print_smt())
print("{months}".format(months=print_smt()))
print("{0}".format(print_smt()))
print("".format(print_smt()))