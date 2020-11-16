# Regarding iin (OOP) whether it's a instance/class/global variable
# depends on if it's a per-Bank thing (instance), a per-TypeOfBank
# thing (class) or it's the same for all types and all banks (global)

# <bjs> wyre: well like I described earlier, if it's logically
# something that each Bank would have it, it's an instance attribute.
# If it's logically something a group of banks would have then it's
# a class attribute. If it's logically something that all banks in
# the world would share, it's global.

# So it's CLEARLY an instance attribute

import random


class Bank:

    def __init__(self, iin):
        self.iin = iin
        self.cards = {}

    def main_loop(self):
        """
        Main menu
        """

        while True:

            print("1. Create an account")
            print("2. Log into account")
            print("0. Exit")
            inp = input()

            if inp == "0":
                print()
                print("Bye!")
                break
            elif inp == "1":
                self.create_card()
                # print(self.cards)
            elif inp == "2":
                self.login()

        exit()

    def create_card(self):
        """Creates a new card method, with a random pin
        and a balance of 0
        """

        bii_raw = random.randrange(0, 10000000000)
        bii = f'{bii_raw:0>10}'
        card_number = self.iin + bii

        pin_raw = random.randrange(0, 10000)
        card_pin = f'{pin_raw:0>4}'

        if card_number not in self.cards:
            self.cards[card_number] = [card_pin, 0]
            print()
            print("Your card has been created")
            print("Your card number:")
            print(card_number)
            print("Your card pin:")
            print(card_pin)
            print()
        else:
            self.create_card()

    def user_area(self, card_number):
        """User menu: check the balance, log out or exit
        """

        while True:

            print()
            print("1. Balance")
            print("2. Log out")
            print("0. Exit")
            inp = input()

            if inp == "0":
                print()
                print("Bye!")
                exit()
            elif inp == "1":
                print()
                print(f"Balance: {self.cards[card_number][1]}")
            elif inp == "2":
                print()
                print("You have successfully logged out!")
                print()
                break

    def login(self):
        """Login method to check if the card number exists and
        if the given pin is correct, once those credencials are
        correct, the user goes into the user area
        """

        print()
        print("Enter your card number: ")
        card_number = str(input())
        print("Enter your card pin: ")
        card_pin = str(input())

        if card_number not in self.cards \
                or self.cards[card_number][0] != card_pin:
            print()
            print("Wrong card number or PIN!")
            print()
            # self.login()
        elif self.cards[card_number][0] == card_pin:
            print()
            print("You have successfully logged in!")
            self.user_area(card_number)


if __name__ == '__main__':
    bank = Bank(iin='400000')
    bank.main_loop()
