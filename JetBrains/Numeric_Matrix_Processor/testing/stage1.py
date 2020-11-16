
def sum_matrices(rows_a, cols_a, a, rows_b, cols_b, b):

    result = []
    if rows_a != rows_b and cols_a != cols_b:
        print("ERROR")
    else:
        for row_i, row in enumerate(a):
            result.append([
                element + b[row_i][index]
                for index, element in enumerate(row)
            ])

    return result


def fill_matrix(rows, cols):

    matrix = []
    for i in range(rows):
        row_i = list(map(int, input().split()))
        if len(row_i) == cols:
            matrix.append(row_i)
        else:
            print("Wrong row length. Try again from the beginning.")
            fill_matrix(rows, cols)

    return matrix


def format_output_matrix(matrix):
    str_matrix = [[str(i) for i in j] for j in matrix]

    for i in str_matrix:
        print(' '.join(i))


class MatrixProcessor:

    def __init__(self, operation):
        self.operation = operation

    def main_func(self):

        rows_a, cols_a = map(int, input().split())
        a = fill_matrix(rows_a, cols_a)
        rows_b, cols_b = map(int, input().split())
        b = fill_matrix(rows_b, cols_b)

        if self.operation == "sum":
            print()
            format_output_matrix(
                sum_matrices(
                    rows_a,
                    cols_a,
                    a,
                    rows_b,
                    cols_b,
                    b
                )
            )

            # print(*sum_matrices())


sum_operation = MatrixProcessor(operation="sum")
sum_operation.main_func()
