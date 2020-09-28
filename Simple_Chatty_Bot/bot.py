def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is "
          + str(age)
          + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print('Completed, have a nice day!')


def question():
    print("Which of these actions will result in TypeError?")
    print("1. Convert a string to a tuple using the tuple() function")
    print("2. Get an element by an index that does not exist in a tuple")
    print("3. Set a new value to a tuple item")
    print("4. Create a singleton tuple using round brackets without the comma")

    while True:
        answer = int(input())
        if answer == 3:
            print("Completed, have a nice day!")
            end()
            break
        else:
            print("Please, try again.")


def end():
    print('Congratulations, have a nice day!')


greet('Boty', '2020')  # change it as you need
remind_name()
guess_age()
count()
question()
