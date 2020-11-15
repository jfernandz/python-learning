# Operation functions
def sum_matrices(rows_a, cols_a, a, rows_b, cols_b, b):
    """Sums two matrices (a and b) given their dimensions
    """

    result = []
    if rows_a != rows_b and cols_a != cols_b:
        print("The operation cannot be performed.")
    else:
        for row_i, row in enumerate(a):
            result.append([
                element + b[row_i][index]
                for index, element in enumerate(row)
            ])

    return result


def scalar_multiply(matrix, scalar):
    """Multiplies a matrix by a scalar
    """

    return [[i*scalar for i in j] for j in matrix]


def multiply_matrices(cols_a, a, rows_b, b):
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
    else:
        print("The operation cannot be performed.")
        # print("Numbers of columns in the first matrix must be "
        #       + "the same than number of rows in the second matrix.")
        # print("\nRun the program again.")
        exit()


def transpose(matrix):
    """Transpose the array to check columns"""
    return list(map(list, zip(*matrix)))


# Auxiliary functions
def fill_matrix(rows, cols):
    """Fills row by row a matrix using first the given dimension,
    it also checks if a given row has the correct number of elements
    """

    # print(str(rows) + "x" + str(cols))
    matrix = []
    for i in range(rows):
        row_i = list(map(float, input().split()))
        if len(row_i) == cols:
            matrix.append(row_i)
        else:
            print("Wrong row elements. Try again from the beginning.")
            # It's important to use the return statement, so the function
            # terminates and we avoid a scoping behaviour
            return fill_matrix(rows, cols)

    # print("Matrix has been filled")
    # print(matrix)
    return matrix


def format_output_matrix(matrix):
    """Formats the output, given a matrix it prints according
    its dimension
    """

    str_matrix = [[str(i) for i in j] for j in matrix]

    for i in str_matrix:
        print(' '.join(i))


def input_dimension(instructions_str):
    try:
        rows, cols = map(int, input(instructions_str).split())
        if rows == 0 or cols == 0:
            print("Dimension must be greater than 0, try again.")
            return input_dimension(instructions_str)
        else:
            return rows, cols
    except (TypeError, ValueError):
        print("You must specify rows x columns.")
        return input_dimension(instructions_str)


# Matrix processor class
class MatrixProcessor:

    def __init__(self, operation):
        self.operation = operation

    def main_selector(self):

        if self.operation == "sum_matrices" or\
                self.operation == "multiply_matrices":
            # print("Adding up matrices")
            rows_a, cols_a = input_dimension(
                "Enter size of first matrix: "
            )

            print("Enter first matrix:")
            a = fill_matrix(rows_a, cols_a)

            rows_b, cols_b = input_dimension(
                "Enter size of second matrix: "
            )

            print("Enter second matrix:")
            b = fill_matrix(rows_b, cols_b)

            print("The result is:")
            if self.operation == "sum_matrices":
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
            elif self.operation == "multiply_matrices":
                format_output_matrix(
                    multiply_matrices(
                        cols_a,
                        a,
                        rows_b,
                        b
                    )
                )

        if self.operation == "scalar_multiply":
            # print("Multiply by scalar")
            rows, cols = input_dimension(
                "Enter size of the matrix: "
            )

            print("Enter matrix:")
            matrix = fill_matrix(rows, cols)

            scalar = float(input("Enter constant: "))

            print("The result is:")
            format_output_matrix(
                scalar_multiply(
                    matrix,
                    scalar
                )
            )


def main_menu():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("0. Exit")
        choice = int(input("Your choice: "))

        if choice == 0:
            exit()
        elif choice == 1:
            sum_op = MatrixProcessor(operation="sum_matrices")
            sum_op.main_selector()
        elif choice == 2:
            scal_mult_op = MatrixProcessor(operation="scalar_multiply")
            scal_mult_op.main_selector()
        elif choice == 3:
            mult_matrices_op = MatrixProcessor(operation="multiply_matrices")
            mult_matrices_op.main_selector()


main_menu()
