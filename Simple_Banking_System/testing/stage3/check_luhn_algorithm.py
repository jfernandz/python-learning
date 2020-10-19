def check_number():
    print("Give me the card number: ")
    card_number = str(input())

    try:
        if luhn_algorithm(card_number[:-1]) == card_number[-1]:
            print("Yes, your card number is apparently correct.")
        else:
            print("Nope, this card number is wrong.")
    except ValueError:
        print("You must introduce numbers")


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


check_number()
