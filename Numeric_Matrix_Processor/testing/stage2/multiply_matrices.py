def transpose(matrix):
    """Transpose the array to check columns"""
    return list(map(list, zip(*matrix)))


def multiply_matrices(rows_a, cols_a, a, rows_b, cols_b, b):
    """Multiplies two matrices
    """

    if cols_a == rows_b:
        result = []
        for ia, row_ia in enumerate(a):
            result.append([])
            for row_ib in transpose(b):
                aux = 0
                for i, elem_a in enumerate(row_ia):
                    aux += elem_a*row_ib[i]
                result[ia].append(aux)

    return result


a = [[1, 7], [2, 5]]
b = [[2, 4], [3, 1]]
# 1 7  2 4    23 11
# 2 5  3 1    19 13
print(a)
print(transpose(b), "<", b)
print(multiply_matrices(2, 2, a, 2, 2, b))
