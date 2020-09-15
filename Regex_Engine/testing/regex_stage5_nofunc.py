# import sys
# sys.setrecursionlimit(10000)


def match_char(single_re, character):
    """Checks if a single character in a string does match
    a single character in a regular expression (taking into
    account also the wild-card '.' character)
    """
    if single_re in (character, "."):
        return True
    else:
        return False


def match_string(re, string):
    """Checks if a regexp-string pair does match. Both of them must
    have the same length!!. i.e. It compares the 're' pattern with
    a given 'string' character by character using match_char()
    function.
    """
    if len(re) == 0:
        # 're' pattern was sliced to the end so this means the 're' pattern
        # WAS found inside 'string'
        print("'regex' was consumed")
        print(f"{re}|{string}")
        return True
    elif len(string) == 0:
        # 'string' was sliced to the end so this means the 're' pattern
        # WASN'T found inside 'string'
        if re == "$":
            # The string was consumed but 're' patter wasn't, however last
            # character in 're' is "$", which is the special character that
            # points the pattern must be located at the and of the string.
            return True
        if re[-1] in ("*", "+"):
            return True
        print("'string' was consumed")
        return False

    # ? operator
    if len(re) > 1 and re[1] == "?":
        return match_string(*question_mark_op(re, string))

    # * operator
    if len(re) > 1 and re[1] == "*":  # and asterisk_op(re, string) is not None
        return match_string(*asterisk_op(re, string))

    # + operator
    if len(re) > 1 and re[1] == "+":  # and plus_op(re, string) is not None:
        return match_string(*plus_op(re, string))

    if match_char(re[0], string[0]):
        # Initial character matches but it keeps looking for the rest of
        # the characters inside 're' patter __recursively__ (by slicing,
        # i.e. incrementing the 're' pattern and the 'string' one position)
        print(f"Main: {re}|{string}")  # Debug
        print(f"Mai-: {re[1:]}|{string[1:]}")  # Important debug
        return match_string(re[1:], string[1:])
    else:
        # Initial character in 'string' did not match the initial character
        # in 're' pattern, so 're' patter WASN'T found.
        return False


def plus_op(re, string):
    # print(f"Func: {re}|{string}")  # Important debug
    if match_char(re[0], string[0]) and len(string) > 1:
        return re, string[1:]
    else:
        return re[2:], string


def asterisk_op(re, string):
    print(f"Func: {re}|{string}")  # Important debug
    if match_char(re[0], string[0]):  # 1st case
        print(f"if -> {re}|{string[1:]}")  # Debug
        return re, string[1:]
    else:
        print(f"elif -> {re[2:]}|{string}")  # Debug
        return re[2:], string


def question_mark_op(re, string):
    if match_char(re[0], string[0]) is False:   # 1st case
        print(f"if -> {re[2:]}|{string}")
        return re[2:], string
    else:
        print(f"el -> {re[2:]}|{string[1:]}")                     # 2nd case
        return re[2:], string[1:]


def find_pattern(re, long_str):
    """Finds the regex pattern inside a longer string"""
    if match_string(re, long_str):
        # 're' pattern WAS found inside long_str or a slice of long_str
        return True
    else:
        if len(long_str) == 0:
            # long_str was sliced to the end and the 're' pattern
            # WASN'T found inside
            return False
        else:
            # It keeps looking the pattern recursively inside long_str
            # but with an incremented starting position
            return find_pattern(re, long_str[1:])


def main_func():

    regex, word = input().split("|")

    if len(regex) != 0 and regex[0] == "^":
        # Non-empty regex was provided and it starts with "^" special
        # character that points the patter must be located at the
        # beggining of the string, this is why check_string() is
        # called directly. (We don't need to look for it in a
        # longer srting)
        print(match_string(regex[1:], word))
    else:
        print(find_pattern(regex, word))


if __name__ == '__main__':
    main_func()
