def final_deposit_amount(*interest, amount=1000):
    # Using recursion instead a for loop
    amount *= (1 + interest[0] / 100)
    if len(interest) == 1:
        return round(amount, 2)
    else:
        return final_deposit_amount(*interest[1:], amount=amount)


print(final_deposit_amount(5, 7, 4))
