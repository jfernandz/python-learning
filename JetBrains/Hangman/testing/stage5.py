import random

random.seed()
print("H A N G M A N")

word_list = ['python', 'java', 'kotlin', 'javascript']
tries = 8
word = word_list[random.randint(0, 3)]

hint = list("-"*len(word))

while tries > 0:
    # if "".join(hint) == word:
    #    print()
    #    break
    print("\n" + "".join(hint))
    letter = input("Input a letter: ")
    if letter in set(word):
        for i, j in enumerate(word):
            if letter == j:
                hint[i] = letter
    else:
        print("The letter doesn't appear in the word")
    tries -= 1

print("""\nThanks for playing!
We'll see how well you did in the next stage""")
