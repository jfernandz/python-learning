def format_line(c_str):
    """"Function to format each line"""
    return ''.join([f' {char}' for char in c_str])

def main():
    cells = str(input("Enter cells: "))

    if len(cells) != 9:
        print("Invalid cells number.")
        exit()

    print('-'*9)
    for i, _ in enumerate(cells[::3]):
     print(f'|{format_line(cells[i*3:i*3+3])} |')
    print('-'*9)

main()
