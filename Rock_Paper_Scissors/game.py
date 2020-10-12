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
    # no_user_opts = [opt for opt in options if opt != user_choice]
    ########################

    no_user_opts = options[options.index(user_choice) + 1:] \
        + options[:options.index(user_choice)]

    user_lose_against = no_user_opts[:len(no_user_opts) // 2]
    user_wins_against = no_user_opts[len(no_user_opts) // 2:]

    if computer_choice in user_wins_against:
        return "win"
    elif computer_choice in user_lose_against:
        return "lose"
    elif computer_choice == user_choice:
        return "draw"
    elif user_choice not in options:
        return "invalid"


def check_list(unsorted_opts):
    comp = ["rock", "gun", "lightning", "devil", "dragon", "water",
            "air", "paper", "sponge", "wolf", "tree", "human",
            "snake", "scissors", "fire"]

    mid = ["rock", "spock", "paper", "lizard", "scissors"]

    simp = ["rock", "paper", "scissors"]

    if len(unsorted_opts) == len(comp):
        return comp
    elif len(unsorted_opts) == len(mid):
        return mid
    elif len(unsorted_opts) == len(simp):
        return simp
    else:
        print("Invalid options list")


def game(unsorted_opts, curr_usr_rat):

    opts = check_list(unsorted_opts)

    while True:
        computer_inp = opts[random.randint(0, len(opts)-1)]
        user_inp = str(input())
        if user_inp in opts:
            if complex_comparator(user_inp, computer_inp, opts) == "win":
                print("Well done. The computer "
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

    user_given_opts = input()
    print("Okay, let's start")
    if not user_given_opts:
        user_given_opts = ["rock", "paper", "scissors"]
        game(user_given_opts, current_user_rating)
    else:
        user_given_opts = user_given_opts.split(",")
        game(user_given_opts, current_user_rating)


if __name__ == '__main__':
    main_func()
