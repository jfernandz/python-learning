def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def calc_factorial():
    x = int(input("Give me a number: "))
    print(f"{x}! = ", factorial(x))


if __name__ == "__main__":
    calc_factorial()
