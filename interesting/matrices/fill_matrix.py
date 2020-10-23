# Given the dimension, this function fills a matrix


def fill_matrix(rows, cols):

    print(str(rows) + "x" + str(cols))
    matrix = []
    for i in range(rows):
        row_i = list(map(int, input().split()))
        if len(row_i) == cols:
            matrix.append(row_i)
        else:
            print("Wrong row length. Try again from the beginning.")
            # This return statement is so important because if we
            # just call the function it will produce a scoping
            # behaviour, and the function will return also bad
            # filled matrices. We need to specify the return
            # so the function terminates and starts from
            # the beginning and do not nest several function
            # instances
            return fill_matrix(rows, cols)

    print("Matrix has been filled")
    print(matrix)
    return matrix


rows, cols = map(int, input().split())
m = fill_matrix(rows, cols)
