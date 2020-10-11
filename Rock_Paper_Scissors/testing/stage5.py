import random


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


def simple_comparator(user_choice, computer_choice, options):
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


def simple_game(opts, curr_usr_rat):

    while True:
        computer_inp = opts[random.randint(0, len(opts)-1)]
        user_inp = str(input())

        if user_inp in opts:
            if simple_comparator(user_inp, computer_inp, opts) == "win":
                print("Well done. The computer"
                      + f"choose {computer_inp} and failed")
                curr_usr_rat += 100
                continue
            elif simple_comparator(user_inp, computer_inp, opts) == "draw":
                print(f"There is a draw ({computer_inp})")
                curr_usr_rat += 50
                continue
            elif simple_comparator(user_inp, computer_inp, opts) == "lose":
                print(f"Sorry, but the computer chose {computer_inp}")
                continue
            elif simple_comparator(user_inp, computer_inp, opts) == "invalid":
                print("Invalid input")
                continue
        elif user_inp == "!rating":
            print(curr_usr_rat)
            continue
        elif user_inp == "!exit":
            print("Bye!")
            break
        else:
            print("Invalid input")

    exit()


def complex_comparator(user_choice, computer_choice, options):
    # The algorithm is basically that we need to remove the user
    # option and the last option in the list must be moved to the
    # first option, then we can slice the list

    ########################
    # Due list are mutable objects, I have two options if I want
    # to preserve the options list,
    # 1 - Make a copy of the list and apply to that copy the remove()
    # no_user_opts = options
    # no_user_opts.remove(user_choice)
    # 2 - Create a new list using list comprehensions
    no_user_opts = [opt for opt in options if opt != user_choice]
    ########################

    fixed_no_user_opts = no_user_opts[-1:] + no_user_opts[:-1]

    user_lose_against = fixed_no_user_opts[:len(fixed_no_user_opts) // 2]
    user_wins_against = fixed_no_user_opts[len(fixed_no_user_opts) // 2:]

    if computer_choice in user_wins_against:
        return "win"
    elif computer_choice in user_lose_against:
        return "lose"
    elif computer_choice == user_choice:
        return "draw"
    elif user_choice not in options:
        return "invalid"


def complex_game(opts, curr_usr_rat):

    while True:
        computer_inp = opts[random.randint(0, len(opts)-1)]
        user_inp = str(input())
        complex_comparator(user_inp, computer_inp, opts)
        if user_inp in opts:
            if complex_comparator(user_inp, computer_inp, opts) == "win":
                print("Well done. The computer"
                      + f"choose {computer_inp} and failed")
                curr_usr_rat += 100
                continue
            elif complex_comparator(user_inp, computer_inp, opts) == "draw":
                print(f"There is a draw ({computer_inp})")
                curr_usr_rat += 50
                continue
            elif complex_comparator(user_inp, computer_inp, opts) == "lose":
                print(f"Sorry, but the computer chose {computer_inp}")
                continue
            elif complex_comparator(user_inp, computer_inp, opts) == "invalid":
                print("Invalid input")
                continue
        elif user_inp == "!rating":
            print(curr_usr_rat)
            continue
        elif user_inp == "!exit":
            print("Bye!")
            break
        else:
            print("Invalid input")

    exit()


def main_func():
    """Main function, it asks for the users name, greets them, call the
    read_ratings() and game() funtions
    """

    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")

    current_user_rating = read_ratings(user_name)

    opts = input()
    print("Okay, let's start")
    if not opts:
        opts = ["rock", "paper", "scissors"]
        simple_game(opts, current_user_rating)
    else:
        opts = opts.split(",")
        complex_game(opts, current_user_rating)


if __name__ == '__main__':
    main_func()
