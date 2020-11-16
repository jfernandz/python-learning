box = [10, 20, 33]

print([candy % 2 for candy in box])

if any([candy % 2 for candy in box]):
    print("It is not a proper gift.")
else:
    print("Perfect!")
