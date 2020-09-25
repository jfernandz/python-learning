import random


def main_func():

    random.seed()
    print("H A N G M A N")

    word_list = ['python', 'java', 'kotlin', 'javascript']
    tries = 8
    word = word_list[random.randint(0, 3)]
    guessed = set()
    win = False

    hint = list("-"*len(word))

    while tries > 0:
        if "".join(hint) == word and tries > 0:
            print()
            win = True
            break
        print("\n" + "".join(hint))
        letter = input("Input a letter: ")
        if letter in set(word) and letter not in guessed:
            guessed.add(letter)
            for i, j in enumerate(word):
                if letter == j:
                    hint[i] = letter
        elif letter in guessed:
            print("No improvements")
            tries -= 1
        else:
            print("That letter doesn't appear in the word")
            tries -= 1

    if win:
        print(word)
        print("You guessed the word!"
              + "\nYou survived!")
    else:
        print("You lost!")


if __name__ == "__main__":
    main_func()
