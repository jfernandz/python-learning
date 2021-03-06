#########################################
# Old functions to print the battleground
#
# def format_line(c_str):
#     """"Function to format each line"""
#     return ''.join([f' {i}' for i in c_str])
#
#
# def print_field(c_str, w):
#     print("-" * w ** 2)
#     for i in range(0, len(c_str), w):
#         print(f'|{format_line(c_str[i:i+w])} |')
#     print("-" * w ** 2)


def print_field_alt(c_str, w):
    """Function to print the battleground. It is necessary to use
    the join() method because strings are immutable, unlike lists,
    that's why this funcion is also using list comprehension.
    c_str -> cells string
    c     -> single cell
    w     -> array width"""
    print("-" * w ** 2)
    for i in range(0, len(c_str), w):
        ####################
        # Debug code
        # print(i)
        # for c in c_str[i:i+w]:
        #     print(c)
        # print([f' {c}' for c in c_str[i:i+w]])
        print('|' + ''.join([f' {c}' for c in c_str[i:i+w]]) + ' |')
    print("-" * w ** 2)


def str_to_array(c_str, w):
    """c_str -> cells string
       c     -> single cell
       w     -> array width"""
    return [[c for c in c_str[i*w:(i+1)*w]] for i in range(w)]


def print_field_array(array):
    """Function to print the battleground from
    an array
    """
    print("-"*len(array)**2)
    for i in array:
        print("| " + ' '.join(i) + " |")
    print("-"*len(array)**2)


def count_symbols(array):
    x = 0
    o = 0
    blank = 0
    for i in array:
        for j in i:
            if j == "X":
                x += 1
            elif j == "O":
                o += 1
            else:
                blank += 1
    if abs(x - o) >= 2:
        print("Impossible")
        exit()
    # print(x, o, blank)


def check_rows(array):
    global x_wins, o_wins
    for i in array:
        for k, j in enumerate(i):
            if k + 1 < len(i) and k - 1 >= 0:
                if i[k] != "_" and i[k] == i[k+1] and i[k] == i[k-1]:
                    # print(f"{i[k]} wins")
                    x_or_o(i[k])


def traspose(array):
    return list(map(list, zip(*array)))


def check_diagonals(array):
    global x_wins, o_wins
    if array[0][0] == array[1][1] == array[2][2]:
        # print(f"{array[0][0]} wins")
        x_or_o(array[0][0])
    elif array[0][2] == array[1][1] == array[2][0]:
        # print(f"{array[0][2]} wins")
        x_or_o(array[0][2])


def x_or_o(symbol):
    global x_wins, o_wins
    if symbol == "X":
        x_wins = True
    if symbol == "O":
        o_wins = True


def main():
    cells = "XXXX_OX_O"
    # cells = str(input("Enter cells: "))
    width = 3

    if len(cells) > 9:
        print("Too many cells.")
        exit()
    elif len(cells) < 9:
        print("Not enough cells.")
    else:
        pass

    # print(format_line(cells))
    # print_field(cells, width)
    # print_field_alt(cells, width)
    print_field_array(str_to_array(cells, width))
    # print_field_array(traspose(str_to_array(cells, width)))
    # print(array(cells, width)[2][2])
    # print_field_nlst(str_to_array(cells, width), width)
    count_symbols(str_to_array(cells, width))
    check_rows(str_to_array(cells, width))
    check_rows(traspose(str_to_array(cells, width)))
    check_diagonals(str_to_array(cells, width))


x_wins = None
o_wins = None

main()

if x_wins is True and o_wins is True:
    print("Impossible")
elif x_wins is True and o_wins is None:
    print("X wins")
elif x_wins is None and o_wins is True:
    print("O wins")
else:
    print("Game not finished")
