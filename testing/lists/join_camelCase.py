text = str(input())
lst = text.split()

for i, j in enumerate(lst):
    if i != 0:
        lst[i] = j.capitalize()

print("".join(lst))
