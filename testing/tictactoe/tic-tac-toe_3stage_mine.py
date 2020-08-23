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


def array(c_str, w):
    """c_str -> cells string
       c     -> single cell
       w     -> array width"""
    return [[c for c in c_str[i*w:(i+1)*w]] for i in range(w)]


def print_field_nlst(c_lst, w):
    for i in range(w):
        print(c_lst[i][i])


def check_rows(array):
    pass


def main():
    cells = "abcdefghi"
    # cells = str(input("Enter cells: "))
    width = 3

    if len(cells) != 9:
        print("Invalid cells number.")
        exit()

    # print(format_line(cells))
    # print_field(cells, width)
    print_field_alt(cells, width)
    # print(array(cells, width)[2][2])
    # print_field_nlst(convert_str_to_array(cells, width), width)


main()
