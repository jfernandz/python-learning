def final_deposit_amount(*interest, amount=1000):
    """Using recursion instead a for loop
    """
    amount *= (1 + interest[0] / 100)
    if len(interest) == 1:
        return round(amount, 2)
    else:
        return final_deposit_amount(*interest[1:], amount=amount)


def final_deposit_amount_v2(*interest, amount=1000):
    """If you find confusing to use 'amount' for both argument
    and parameter and you want to make the difference you cannot
    use the `*=` operator
    """
    new_amount = amount * (1 + interest[0] / 100)
    if len(interest) == 1:
        return round(new_amount, 2)
    else:
        return final_deposit_amount_v2(*interest[1:], amount=new_amount)


# print(final_deposit_amount(5, 7, 4))
print(final_deposit_amount_v2(5, 7, 4))
