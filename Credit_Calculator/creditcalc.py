# ################################################
# Definitions pattern for all functions:
# t -> '-t', '--type'      Type of calculation the program must perform, is always required.
# p -> '-p', '--principal' Credit principal. It Might not be required when --type=annuity
# a -> '-a', '--payment'   Monthly payments (annuity) when the program does not calculates
#                          the differentiated payment. This parameter is not required
#                          when --type=diff
# n -> '-n', '--periods'   Periods (months). This parameter might not be required when
#                          --type=annuity
# i -> '-i', '--interest'  Interest rate. It must be divided by 100 and 12 because is
#                          annual percentage, this is done when proc_args list is created.
#                          It's always required.
# ################################################

import math
import argparse


def error_msg():
    """Just to print the error msg and terminate the program"""
    print("Incorrect parameters.")
    exit()


def check_args_number(args_list):
    """Counts the unset arguments. Default values are None, so
    when any argument is None in the list, n_nones variable increments
    by 1. Then if n_nones >= 2 or <= 0, it throws the error msg"""
    n_nones = 0
    for j in range(len(args_list)):
        if args_list[j] is None:
            n_nones += 1
    if n_nones >= 2 or n_nones == 0:
        error_msg()


def check_undef_and_values(t, p, a, n, i):
    """Checks first if type or interest are given in the command line,
    After this checks if some other value is negative. This first part
    could be done with 'require=True' argument in argparse, but JetBrains
    wants a specific error message."""
    if t is None or i is None:
        error_msg()
    if p is None:
        if a <= 0 or n <= 0 or i < 0:
            error_msg()
    elif a is None:
        if p <= 0 or n <= 0 or i < 0:
            error_msg()
    elif n is None:
        if a <= 0 or p <= 0 or i < 0:
            error_msg()


def check_type_do_calculations(t, p, a, n, i):
    """Checks which type was selected and calls the proper
    function in order to perform the right calculations"""
    if t == "annuity":
        annuity_calculations(p, a, n, i)
    elif t == "diff":
        diff_calculations(p, a, n, i)
    else:            # This block should not be necessary because --type arg has 'choices'
        error_msg()  # option enabled in argparse when it is parsed in main() function


def diff_calculations(p, a, n, i):
    """Do the proper calculations when --type=diff. This function also checks
    that a (payment) is undefined. When different payments are calculated
    for each month the user cannot specify a payment (annuity)"""
    if a is not None:
        error_msg()
    else:
        total_paid = 0
        for m in range(1, n + 1):
            diff_payment = math.ceil((p / n) + i * (p - (p * (m - 1) / n)))
            print(f"Month {m}: paid out {diff_payment}")
            total_paid += diff_payment
        print("Overpayment = {}".format(math.ceil(total_paid - p)))


def annuity_calculations(p, a, n, i):
    """Calls the proper function according to the unset (undefined) argument
    (set as None) when the program is run in the command line"""
    if a is None:
        a_calc_annuity(p, n, i)
    elif p is None:
        a_calc_principal(a, n, i)
    elif n is None:
        a_calc_periods(p, a, i)


def a_calc_annuity(p, n, i):
    """Calculates the annuity payments and the Overpayment
    caused by the interest rate"""
    if i == 0:
        annuity = math.ceil(p / n)
        print(f"Your annuity payment = {annuity}!")
    else:
        annuity = math.ceil(p * i * (1 + i) ** n / (math.pow((1 + i), n) - 1))
        print(f"Your annuity payment = {annuity}!")
        op = annuity * n - p
        print(f"Overpayment = {op}")


def a_calc_principal(a, n, i):
    """Calculates the total credit amount (principal) and
    an Overpayment caused by the interest rate"""
    principal_ni = a * n
    if i == 0:
        print(f"Your credit principal = {math.floor(principal_ni)}!")
    else:
        principal = a * (pow((1 + i), n) - 1) / i / pow((1 + i), n)
        print(f"Your credit principal = {math.floor(principal)}!")
        print("Overpayment = {}".format(math.ceil(principal_ni - principal)))


def a_calc_periods(p, a, i):
    """Calculates the necessary periods to repay the credit and
    the Overpayment due to the interest rate"""
    if i == 0:
        months = math.ceil(p / a)
        years = months // 12
        remainder_months = months % 12
        print(f"You need {years} years and {remainder_months} months to repay this credit!")
    else:
        months = round(math.log(a / (a - i * p), 1 + i))
        if months == 12:
            print("You need 1 year to repay this credit!")
        elif months >= 12:
            years = months // 12
            remainder_months = months % 12
            if remainder_months == 0:
                print(f"You need {years} years to repay this credit!")
                print("Overpayment = {}".format(math.ceil(months * a - p)))
            else:
                print(f"You need {years} years and {remainder_months} months to repay this credit!")
                print("Overpayment = {}".format(math.ceil(months * a - p)))
        else:
            print(f"You need {months} to repay this credit!")
            print("Overpayment = {}".format(math.ceil(months * a - p)))


def main():
    """Main function.
    It parses the command line arguments, --type and --interest
    should be 'required=True', however, JetBrains academy expects
    a specific error message defined in error_msg() function at line 5"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type",
                        type=str,
                        # required=True,
                        choices=['diff', 'annuity'],
                        help="Indicates the type of payment")
    parser.add_argument("-p", "--principal",
                        type=int,
                        help="Credit principal amount")
    parser.add_argument("-a", "--payment",
                        type=float,
                        help="Monthly payments")
    parser.add_argument("-n", "--periods",
                        type=int,
                        help="Number of months")
    parser.add_argument("-i", "--interest",
                        type=float,
                        # required=True,
                        help="Annual interest (must be specified without percent symbol)")
    args = parser.parse_args()

    # List to gather all raw arguments and check how many are undefined.
    # Mainly --type and --interest, which cannot be None under any circumstances.
    raw_args = [args.type,
                args.principal,
                args.payment,
                args.periods,
                args.interest]

    # Checking number of arguments
    check_args_number(raw_args)

    # Checking if --type is not given. I prefer to use the argument required=True from
    # argparse module, but JetBrains Academy wants a specific error message.
    # IMPORTANT:
    # I'm using here the asterisk as 'iterable unpacking operator' because I don't
    # want to pass the list itself but the elements inside as different arguments.
    # https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
    check_undef_and_values(*raw_args)

    # Creating a list with processed arguments like interest, which must be divided
    # by 100 and 12 because is an annual percentage. This is needed because first
    # the program must check that args.interest is not None (undefined) and in the
    # case is undefined (None) it cannot be divided.
    proc_args = [args.type,
                 args.principal,
                 args.payment,
                 args.periods,
                 args.interest / 100 / 12]

    # Checks --types argument and according the given value do the proper calculations.
    check_type_do_calculations(*proc_args)


main()

