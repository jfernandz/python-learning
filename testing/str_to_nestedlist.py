cells = "abcdefghi"

############################
# Made by bruteforce:
#
# matrix = []
# k = 0
# for i in range(3):
#     matrix.append([])
#     for j in range(3):
#         # print(cells[k])
#         matrix[i].append(cells[k])
#         k += 1
#
# print(matrix)


############################
# Explicit for loop but with enumerate:
#
matrix = []
for i in range(3):
    matrix.append([])
    for j, cell in enumerate(cells[i*3:(i+1)*3]):
        # Debug prints
        print(f"Slice indexes: cells[{i*3}:{(i+1)*3}]")
        print(list(enumerate(cells[i*3:(i+1)*3])))
        print("Enum indexes and cell:", f"({j}, '{str(cell)}')")
        print("\n")
        ##############
        matrix[i].append(cell)

print(matrix)


############################
# Nested list comprehension:
#
print([[cell for _, cell in enumerate(cells[i*3:(i+1)*3])] for i in range(3)])
