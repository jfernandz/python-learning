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
import sqlite3


class Bank:

    def __init__(self, iin, db_file):
        self.iin = iin
        self.conn = self.create_connection(db_file)

        if self.conn is not None:
            self.cur = self.conn.cursor()
            self.create_table()
        else:
            print("Error! Cannot create the database connection.")

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
            elif inp == "2":
                self.login()

        exit()

    @staticmethod
    def create_connection(db_file):
        """Crates database connection
        """

        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error:
            print(sqlite3.Error)

        return conn

    def create_table(self):
        """Creates main table to store cards info (I would have called it
        `cards` but JetBrains requirements were to call it `card` among
        other things I consider wrong, I prefer my creation query, which
        is commented)
        """
        # create_query = """CREATE TABLE IF NOT EXISTS cards (
        #                     id INTEGER PRIMARY KEY AUTOINCREMENT,
        #                     number VARCHAR(16) UNIQUE,
        #                     pin VARCHAR(4),
        #                     balance INTEGER DEFAULT 0
        #                   );"""

        create_query = """CREATE TABLE IF NOT EXISTS card (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            number TEXT UNIQUE,
                            pin TEXT,
                            balance INTEGER DEFAULT 0
                          );"""

        try:
            self.cur.execute(create_query)
        except sqlite3.Error:
            print(sqlite3.Error)

    def all_cards_list(self):
        """Fetches all existent cards in a list.
        """
        try:
            self.cur.execute("SELECT number FROM card;")
        except sqlite3.Error:
            print(sqlite3.Error)

        return list(*zip(*self.cur.fetchall()))

    def gen_card_number(self):
        """Generates a random card number
        """

        bii_raw = random.randrange(0, 1000000000)
        bii = f'{bii_raw:0>9}'
        iin_bii = self.iin + bii

        return iin_bii + self.luhn_algorithm(iin_bii)

    def gen_unique_card_number(self):
        """Checks if a particular card number is already in the db (by
        calling all_cards_list() method). This is a recursive method
        because is calling itself when the card number is not unique,
        it's also calling gen_card_number() method to generate many
        card numbers as needed.
        """
        all_cards_list = self.all_cards_list()

        number = self.gen_card_number()
        if number not in all_cards_list:
            return number
        else:
            return self.gen_unique_card_number()

    def create_card(self):
        """Creates a new card method, with a random pin
        and a balance of 0
        """

        card_number = self.gen_unique_card_number()

        pin_raw = random.randrange(0, 10000)
        card_pin = f'{pin_raw:0>4}'

        try:
            insert_query = """INSERT INTO card (
                                number,
                                pin,
                                balance
                               )
                               VALUES (
                                :card_number,
                                :card_pin,
                                0
                               );"""

            self.cur.execute(
                insert_query,
                {"card_number": card_number,
                 "card_pin": card_pin}
            )

            self.conn.commit()
            print()
            print("Your card has been created")
            print("Your card number:")
            print(card_number)
            print("Your card pin:")
            print(card_pin)
            print()
        except sqlite3.Error:
            print(sqlite3.Error)

    @staticmethod
    def luhn_algorithm(iin_bii):
        """Static method to calc the last digit fulfilling
        the luhn algorithm
        """
        iin_bii_list = [int(i) for i in iin_bii]
        for index, _ in enumerate(iin_bii_list):
            # Remember that for iterable objects first index is 0
            # and for this luhn algorithm, the numbers in odd positions
            # must be multiplied by 2, so the first one (1 but 0 index)
            # must be multiplied; so we have to check if (index + 1) % 2 == 1
            # and when index = 0 -> (0 + 1) % 2 = 1, so it will be multiplied
            if (index + 1) % 2 == 1:
                iin_bii_list[index] *= 2
                if iin_bii_list[index] > 9:
                    iin_bii_list[index] -= 9

        n = 0
        while (sum(iin_bii_list) + n) % 10 != 0:
            n += 1

        return str(n)

    def fetch_pin(self, card_number):
        """Fetches the pin for a particular given card_number
        """
        fetch_pin_query = """SELECT
                                pin
                             FROM
                                card
                            WHERE
                                number=:card_number
                            ;"""

        try:
            self.cur.execute(
                fetch_pin_query,
                {"card_number": card_number}
            )
        except sqlite3.Error:
            print(sqlite3.Error)

        return str(*self.cur.fetchone())

    def login(self):
        """Login method to check if the card number exists and
        if the given pin is correct, once those credentials are
        correct, the user goes into the user area
        """

        print()
        print("Enter your card number: ")
        card_number = str(input())
        print("Enter your card pin: ")
        card_pin = str(input())

        all_card_list = self.all_cards_list()
        # print(self.all_cards_list(), self.fetch_pin(card_number))  # Debug
        if card_number in all_card_list \
                and card_pin == self.fetch_pin(card_number):
            print()
            print("You have successfully logged in!")
            self.user_area(card_number)
        else:
            print()
            print("Wrong card number or PIN!")
            print()

    def fetch_balance(self, card_number):
        """Fetches the balance available in a particular given card_number
        """
        balance_query = """SELECT
                                balance
                            FROM
                                card
                            WHERE
                                number=:card_number
                         ;"""

        try:
            self.cur.execute(
                balance_query,
                {"card_number": card_number}
            )
        except sqlite3.Error:
            print(sqlite3.Error)

        return str(*self.cur.fetchone())

    def user_area(self, card_number):
        """User menu: check the balance, log out or exit
        """
        balance = self.fetch_balance(card_number)

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
                print(f"Balance: {balance}")
            elif inp == "2":
                print()
                print("You have successfully logged out!")
                print()
                break


if __name__ == '__main__':
    bank = Bank(iin='400000', db_file='card.s3db')
    bank.main_loop()
