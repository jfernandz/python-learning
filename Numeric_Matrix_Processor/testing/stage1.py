
def sum_matrices():
    rows_a, cols_a = map(int, input().split())
    a = fill_matrix(rows_a, cols_a)
    rows_b, cols_b = map(int, input().split())
    b = fill_matrix(rows_b, cols_b)

    if rows_a != rows_b and cols_a != cols_b:
        print("ERROR")
    else:
        result = []
    return a, b


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


class MatrixProcessor:

    def __init__(self, operation):
        self.operation = operation

    def main_func(self):

        if self.operation == "sum":
            print(sum_matrices())
            # print(*sum_matrices())


sum_operation = MatrixProcessor(operation="sum")
sum_operation.main_func()
