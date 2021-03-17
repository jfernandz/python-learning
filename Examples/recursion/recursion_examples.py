#!/usr/bin/env python


print("""
███████╗██╗██████╗  ██████╗ ███╗   ██╗ █████╗  ██████╗ ██████╗██╗
██╔════╝██║██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██╔════╝██╔════╝██║
█████╗  ██║██████╔╝██║   ██║██╔██╗ ██║███████║██║     ██║     ██║
██╔══╝  ██║██╔══██╗██║   ██║██║╚██╗██║██╔══██║██║     ██║     ██║
██║     ██║██████╔╝╚██████╔╝██║ ╚████║██║  ██║╚██████╗╚██████╗██║
╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚═╝
""")


#######################################
# Fibonacci recursive funtion to compute the value for any i-th term
#######################################
def fib_rec(i):
    if i <= 1:
        return i
    elif i == 2:
        return 1
    else:
        return fib_rec(i-1) + fib_rec(i-2)


#######################################
# For loop way to do the same
#######################################
def fib_for(m):
    fib_seq = [0, 1]
    if m == 0:
        return fib_seq[0]
    elif m == 1:
        return fib_seq[1]
    elif m >= 2:
        for i in range(2, m+1):
            next_term = fib_seq[i-1] + fib_seq[i-2]
            fib_seq.append(next_term)
        return fib_seq[-1]


#######################################
# Function to show *all preceding values for all preceding terms* for a given n-th term
# and to show how each is calculated
#######################################
def calc_terms_fib(n, fib_func):
    for i in range(n+1):

        print("#"*50)
        # Single print where you can see the value for the i-th term of all n terms
        print(
            f"Single calc for {i}-th term:",
            f"\nfib({i}) = {fib_func(i)}",
        )
        print("-"*50)

        # For loop to see in detail how each i-th term is calculated, I'm using a generic fib_func()
        # function because I can pass any function as argument in this function, so since I have the
        # functions fib_rec() and fib_for() I can take advantage of them to show all the values for
        # all the terms in every calculation.
        print(
            f"For loop to show detailed calcs for {i}-th term:"
        )
        padding = 0
        for j in range(i, -1, -1):
            if j > 1:
                print(
                    " "*padding +
                    f"fib({j}) = fib({j-1}) + fib({j-2}) = {fib_func(j-1)} + {fib_func(j-2)} = {fib_func(j)}"
                )
            elif j == 1:
                print(
                    " "*padding +
                    "~"*5 +
                    " particular cases " +
                    "~"*5
                )
                print(
                    " "*padding +
                    f"fib({j}) = 1"
                )
            elif j == 0:
                print(
                    " "*padding +
                    f"fib({j}) = 0"
                )

            padding += len("fib(") + len(str(j)) + len(") = ")
        print("-"*50 + "\n"*3)


fib_terms = int(input("How many terms do you want to calculate for the Fibonacci sequence? "))

print("""
██████╗ ███████╗ ██████╗██╗   ██╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔════╝██║   ██║██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║
██████╔╝█████╗  ██║     ██║   ██║██████╔╝███████╗██║██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██║     ██║   ██║██╔══██╗╚════██║██║██║   ██║██║╚██╗██║
██║  ██║███████╗╚██████╗╚██████╔╝██║  ██║███████║██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
""")

calc_terms_fib(fib_terms, fib_rec)

print("""
███████╗ ██████╗ ██████╗     ██╗      ██████╗  ██████╗ ██████╗
██╔════╝██╔═══██╗██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██╔══██╗
█████╗  ██║   ██║██████╔╝    ██║     ██║   ██║██║   ██║██████╔╝
██╔══╝  ██║   ██║██╔══██╗    ██║     ██║   ██║██║   ██║██╔═══╝
██║     ╚██████╔╝██║  ██║    ███████╗╚██████╔╝╚██████╔╝██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝
""")

calc_terms_fib(fib_terms, fib_for)


##################################################################################
##################################################################################
##################################################################################


print("""
███████╗ █████╗  ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗ ██╗
██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗██║
█████╗  ███████║██║        ██║   ██║   ██║██████╔╝██║███████║██║
██╔══╝  ██╔══██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║██║
██║     ██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝
""")


#######################################
# Factorial function to calculate the n-th term with recursion.
#######################################
def fact_rec(m):
    if m == 0:
        return 1
    elif m == 1:
        return 1
    elif m > 1:
        return m*fact_rec(m-1)


#######################################
# Factorial function to calculate the n-th term with a for loop.
#######################################
def fact_for(m):
    fact_seq = [1, 1]
    for i in range(2, m+1):
        fact_seq.append(i*fact_seq[i-1])
    return fact_seq[-1]


#######################################
# Function to enhance the process and how each term in the sequence is calculated
#######################################
def calc_terms_fact(n, fact_func):
    for i in range(n+1):

        print("#"*50)
        # Single print where you can see the value for the i-th term of all n terms
        print(
            f"Single calc for {i}-th term:",
            f"\n{i}! = {fact_func(i)}",
        )
        print("-"*50)

        # For loop to see in detail how each i-th term is calculated, I'm using a generic fact_func()
        # Since I have the fact_rec() and fact_for() functions I can use whatever I want by passing
        # each one as an argument of this function
        print(
            f"For loop to show detailed calcs for {i}-th term:"
        )

        padding = 0
        for j in range(i, -1, -1):
            if j > 0:
                prefix = f"{j}! = "
            else:
                prefix = f"{j}!"

            aligned = ""

            if j > 0:
                for k in range(j, j-2, -1):
                    if k == j:
                        prefix += f"{k}·"
                    elif k < j:
                        aligned += f"{k}!"

            print(f"{' '*padding}{prefix}{aligned} = {fact_func(j)}")
            padding += len(prefix)

        print("-"*50 + "\n"*3)


fact_terms = int(input("What factorial do you want to calculate? "))

print("""
██████╗ ███████╗ ██████╗██╗   ██╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔════╝██║   ██║██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║
██████╔╝█████╗  ██║     ██║   ██║██████╔╝███████╗██║██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██║     ██║   ██║██╔══██╗╚════██║██║██║   ██║██║╚██╗██║
██║  ██║███████╗╚██████╗╚██████╔╝██║  ██║███████║██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
""")

calc_terms_fact(fact_terms, fact_rec)

print("""
███████╗ ██████╗ ██████╗     ██╗      ██████╗  ██████╗ ██████╗
██╔════╝██╔═══██╗██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██╔══██╗
█████╗  ██║   ██║██████╔╝    ██║     ██║   ██║██║   ██║██████╔╝
██╔══╝  ██║   ██║██╔══██╗    ██║     ██║   ██║██║   ██║██╔═══╝
██║     ╚██████╔╝██║  ██║    ███████╗╚██████╔╝╚██████╔╝██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝
""")

calc_terms_fact(fact_terms, fact_for)


##################################################################################
##################################################################################
##################################################################################


# ██████╗  ██████╗ ███╗   ██╗██╗   ██╗███████╗
# ██╔══██╗██╔═══██╗████╗  ██║██║   ██║██╔════╝
# ██████╔╝██║   ██║██╔██╗ ██║██║   ██║███████╗
# ██╔══██╗██║   ██║██║╚██╗██║██║   ██║╚════██║
# ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████║
# ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝


#######################################
# Another example of a Fibonacci sequence which shows all terms whose values are less than a given value.
# This is a little bit trickier but it's so elegant
#######################################
# def rec_fib(n):
#     global iteration
#     a, b = 0, 1
#     while a < n:
#         print(f"fib({iteration}) =", a)
#         a, b = b, a + b
#         iteration += 1
#     print(#)##
# print("Another example:")
# iteration = 0
# rec_fib(100)


# #######################################
# Recursion example with nested behaviour
# #######################################
# def rec_count(number):
#     print("first", number)
#     if number == 0:
#         print("it was 0")
#         return 0
#     rec_count(number - 1)
#     print("next", number)
#
#
# rec_count(3)
