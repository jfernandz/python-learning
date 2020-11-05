def transpose(matrix):
    """Transpose the array to check columns"""
    return list(map(list, zip(*matrix)))


def multiply_matrices(rows_a, cols_a, a, rows_b, cols_b, b):
    """Multiplies two matrices
    """

    if cols_a == rows_b:
        result = []
        for row_ia in a:
            aux = 0
            for element_a in row_ia:
                for row_ib in transpose(b):
                    for element_b in row_ib:
                        print(element_a, element_b, element_a*element_b)
                        aux += element_a*element_b
                        print(aux)
                print(aux)
                result.append(aux)

        return result


a = [[1, 7], [2, 5]]
b = [[2, 4], [3, 1]]
print(a)
print(transpose(b))
print(multiply_matrices(2, 2, a, 2, 2, b))
