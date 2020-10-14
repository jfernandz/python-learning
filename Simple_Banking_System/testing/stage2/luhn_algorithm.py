import random


def create_card():
    """Creates a new card method, with a random pin
    and a balance of 0
    """

    bii_raw = random.randrange(0, 1000000000)
    bii = f'{bii_raw:0>9}'
    iin_bii = iin + bii

    card_number = iin + bii + luhn_algorithm(iin_bii)

    pin_raw = random.randrange(0, 10000)
    card_pin = f'{pin_raw:0>4}'

    if card_number not in cards:
        cards[card_number] = [card_pin, 0]
        print()
        print("Your card has been created")
        print("Your card number:")
        print(card_number)
        print("Your card pin:")
        print(card_pin)
        print()
    else:
        create_card()


def luhn_algorithm(iin_bii):

    iin_bii_list = [int(i) for i in iin_bii]
    print(iin_bii_list)

    for index, _ in enumerate(iin_bii_list):
        if (index + 1) % 2 == 1:
            iin_bii_list[index] *= 2
            if iin_bii_list[index] > 9:
                iin_bii_list[index] -= 9

    print(iin_bii_list)

    n = 0
    while (sum(iin_bii_list) + n) % 10 != 0:
        n += 1

    print(sum(iin_bii_list), "+", str(n), "=", sum(iin_bii_list) + n)
    return str(n)


iin = "400000"
cards = {}
create_card()
