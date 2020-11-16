# It's wrong because two reasons:
# 1 - range() method is generating a range starting at 1!,
#     so is not taking account the first number
# 2 - numbers[i] % 4 == 0 is not a proper condition because
#     number 2 is excluded and it's even
def count_even(numbers):
    counter = 0

    for i in range(1, len(numbers)):
        if numbers[i] % 4 == 0:
            counter += 1

    return counter


n1 = [3, 1, 2, 8, 12, 3]
n2 = [7, 5, 1, 3, 9, 11]
n3 = [1, 3, 8, 5, 7]
n4 = [4, 1, 3, 4, 8, 5]
n5 = [3, 5, 9, 12, 15, 20]


print(f"{n1} has", count_even(n1), "even numbers\n")
print(f"{n2} has", count_even(n2), "even numbers\n")
print(f"{n3} has", count_even(n3), "even numbers\n")
print(f"{n4} has", count_even(n4), "even numbers\n")
print(f"{n5} has", count_even(n5), "even numbers\n")


# Right implementation
def count_even_n(numbers):
    counter = 0

    for i in numbers:
        if i % 2 == 0:
            counter += 1

    return counter


print("-"*30)
print(f"{n1} has", count_even_n(n1), "even numbers\n")
print(f"{n2} has", count_even_n(n2), "even numbers\n")
print(f"{n3} has", count_even_n(n3), "even numbers\n")
print(f"{n4} has", count_even_n(n4), "even numbers\n")
print(f"{n5} has", count_even_n(n5), "even numbers\n")
