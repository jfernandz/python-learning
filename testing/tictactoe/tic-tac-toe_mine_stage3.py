def format_line(c_str):
    """"Function to format each line"""
    return ''.join([f' {i}' for i in c_str])


def print_field(c_str):
    print("-"*9)
    for i in range(0, len(c_str) - 1, 3):
        print(f'|{format_line(c_str[i:i+3])} |')
    print("-"*9)


def convert_str_to_array(c_s, w):
    """c_s -> cells string
       c   -> single cell
       w   -> array width"""
    return [[c for c in c_s[i*w:(i+1)*w]] for i in range(w)]


def main():
    cells = str(input("Enter cells: "))

    if len(cells) != 9:
        print("Invalid cells number.")
        exit()

    print_field(cells)


main()
