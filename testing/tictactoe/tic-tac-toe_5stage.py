# Tic Tac Toe stage 5

def print_field_array(array):
    """Prints the battleground from
    an array
    """
    print("-"*len(array)**2)
    for i in array:
        print("| " + ' '.join(i) + " |")
    print("-"*len(array)**2)


def transport_coords(a, b):
    """
    Translates the coordinates to the (x, y) system
    (x,y) ↦ (3-b, a-1)
    """
    return 3 - b, a - 1


def empty_array(w):
    """Generates an empty array for the start of the game"""
    return [[" " for i in range(w)] for j in range(w)]


def check_rows(array):
    """Checks if some player made a row"""
    for i in array:
        for k, j in enumerate(i):
            if k + 1 < len(i) and k - 1 >= 0:
                if i[k] != " " and i[k] == i[k+1] and i[k] == i[k-1]:
                    print(f"{i[k]} wins")
                    return True


def transpose(array):
    """Transpose the array to check columns"""
    return list(map(list, zip(*array)))


def check_diagonals(array):
    """Checks diagonals (in the case the central cell
    is not empty)"""
    if array[1][1] != " ":
        if array[0][0] == array[1][1] == array[2][2]:
            print(f"{array[0][0]} wins")
            return True
        elif array[0][2] == array[1][1] == array[2][0]:
            print(f"{array[0][2]} wins")
            return True


def check_winner(array):
    """If somebody wins returns True in order to break
    the infinite while loop"""
    if check_diagonals(array):
        return True
    if check_rows(array):
        return True
    if check_rows(transpose(array)):
        return True


def main():
    """Main function; prints the empty field at starting, and
    launch an infinite loop to handle coordinates given by
    players. When there are appropriate coordinates, turn is
    checked, symbol is printed and check_winner() is triggered.
    If there is a winner, the infinite loop is broken."""
    turn = 1

    field = empty_array(3)
    print_field_array(field)

    while True:
        try:
            coords = input("Enter the coordinates: ").split()
            x, y = transport_coords(int(coords[0]), int(coords[1]))
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Coordinates should be from 1 to 3!")
            elif field[x][y] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                if turn % 2 == 1:
                    field[x][y] = "X"
                    print_field_array(field)
                    if check_winner(field):
                        break
                elif turn % 2 == 0:
                    field[x][y] = "O"
                    print_field_array(field)
                    if check_winner(field):
                        break
                turn += 1
                if turn > 9:
                    print("Draw")
                    break
        except (ValueError, IndexError):
            print("You should enter numbers!")


main()
