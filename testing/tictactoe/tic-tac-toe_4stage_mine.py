# Stage 4 of tic tac toe


def str_to_array(c_str, w):
    """c_str -> cells string
       c     -> single cell
       w     -> array width"""
    return [[c for c in c_str[i*w:(i+1)*w]] for i in range(w)]


def str_to_array_exp(c_str, w):
    array = []
    for i in range(w):
        array.append([])
        for c in c_str[i*w:(i+1)*w]:
            if c != "_":
                array[i].append(c)
            else:
                array[i].append(" ")
    return array


def print_field_array(array):
    """Function to print the battleground from
    an array
    """
    print("-"*len(array)**2)
    for i in array:
        print("| " + ' '.join(i) + " |")
    print("-"*len(array)**2)


def transport_coords(a, b):
    """
    (x,y) ↦ (3-b, a-1)
    """
    return 3 - b, a - 1


def main():
    cells = "X_X_O____"
    width = 3

    field = str_to_array_exp(cells, width)
    print_field_array(field)

    while True:
        try:
            coords = input("Enter the coordinates: ").split()
            x, y = transport_coords(int(coords[0]), int(coords[1]))
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Coordinates should be from 1 to 3!")
                continue
            elif field[x][y] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                # print(f"x = {x}", f"y = {y}")
                field[x][y] = "X"
                print_field_array(field)
                break
        except ValueError:
            print("You should enter numbers!")


main()
