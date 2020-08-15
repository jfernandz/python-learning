def format_line(c_str):
    """"Function to format each line"""
    c_list = list(c_str)
    c_list = [' ' + i for i in c_list]
    c_list.insert(0, "|")
    c_list.append(" |")
    return ''.join(c_list)


def main():
    cells = str(input("Enter cells: "))

    if len(cells) != 9:
        print("Invalid cells number.")
        exit()

    first_line = cells[0:3]
    second_line = cells[3:6]
    third_line = cells[6:9]

    print("---------")
    print(format_line(first_line))
    print(format_line(second_line))
    print(format_line(third_line))
    print("---------")


main()
