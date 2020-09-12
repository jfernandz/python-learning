#####################################
# Factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#####################################


#####################################
# Check if a number is power of two
def check_if_power_of_two(n):
    if n == 1:
        return True
    if 1 < n < 2:
        return False
    if n >= 2:
        return check_if_power_of_two(n / 2)
#####################################


#####################################
# Input and main function
def input_number():
    x = int(input("Enter an integer: "))
    print(f"{x}! = ", factorial(x))
    if check_if_power_of_two(x):
        print(f"{x} CAN be obtained as power of two")
    else:
        print(f"{x} CANNOT be obtained as power of two")
#####################################


if __name__ == "__main__":
    input_number()
