import random


def compare(user_choice, computer_choice, options):
    """Compares user and computer option and check who wins
    """

    counters = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

    if user_choice == counters[computer_choice]:
        return "win"
    elif user_choice != computer_choice:
        return "lose"
    elif user_choice == computer_choice:
        return "draw"
    elif user_choice not in options:
        return "invalid"


def read_ratings(user):
    """Reads the rating file and stores the content in a dictionary
    to look for the rating for a particular user
    """

    rating_file = open('rating.txt', 'r')

    # The warning in PyCharm is due I should parse the file first to
    # ensure all lines have only two fields
    rating_dict = dict(
        line.split()
        for line in rating_file.readlines()
        if len(line.split()) == 2
    )

    if user in rating_dict:
        user_rating = int(rating_dict[user])
    else:
        user_rating = 0

    rating_file.close()
    return user_rating


def main_loop():
    """Main function, it asks for the users name, greets them, call the
    read_ratings() funtion and contains the main while loop, which is
    run forever until the user types `!exit` command
    """

    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")

    current_user_rating = read_ratings(user_name)

    opts = ["rock", "paper", "scissors"]

    while True:
        computer_inp = opts[random.randint(0, 2)]
        user_inp = str(input())
        if user_inp in opts:
            if compare(user_inp, computer_inp, opts) == "win":
                print("Well done. The computer"
                      + f"choose {computer_inp} and failed")
                current_user_rating += 100
                continue
            elif compare(user_inp, computer_inp, opts) == "draw":
                print(f"There is a draw ({computer_inp})")
                current_user_rating += 50
                continue
            elif compare(user_inp, computer_inp, opts) == "lose":
                print(f"Sorry, but the computer chose {computer_inp}")
                continue
            elif compare(user_inp, computer_inp, opts) == "invalid":
                print("Invalid input")
                continue
        elif user_inp == "!rating":
            print(current_user_rating)
            continue
        elif user_inp == "!exit":
            print("Bye!")
            break
        else:
            print("Invalid input")

    exit()


if __name__ == '__main__':
    main_loop()
