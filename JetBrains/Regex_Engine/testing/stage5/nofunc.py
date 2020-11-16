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
    # print(f"--------> {re}|{string}")  # Debug
    global plus_flag
    if len(re) == 0:
        # 're' pattern was sliced to the end so this means the 're' pattern
        # WAS found inside 'string'
        # print("'regex' was consumed")  # Debug
        # print(f"{re}|{string}")  # Debug
        return True
    elif len(string) == 0:
        # 'string' was sliced to the end so this means the 're' pattern
        # WASN'T found inside 'string'
        if re == "$":
            # The string was consumed but 're' patter wasn't, however last
            # character in 're' is "$", which is the special character that
            # points the pattern must be located at the and of the string.
            # print('Last character in "re" was "$"')  # Debug
            return True
        # if len(re) == 2 and re[-1] in ("*", "?"):
        #     # print('Last character is "*" or "?"')  # Debug
        #     return match_string(re[2:], string)
        # elif len(re) == 2 and re[-1] == "+" and plus_flag is True:
        #     return match_string(re[2:], string)
        # print("'string' was consumed")  # Debug
        return False

    if match_char(re[0], string[0]):
        if re[1:].startswith("?"):
            return match_string(re[2:], string[1:])
        if re[1:].startswith("*") or re[1:].startswith("+"):
            if re[1:].startswith("+"):
                plus_flag = True
            return match_string(re, string[1:])
        else:
            return match_string(re[1:], string[1:])
    else:
        if re[1:].startswith("?") or re[1:].startswith("*"):
            return match_string(re[2:], string)
        elif re[1:].startswith("+"):
            if plus_flag:
                return match_string(re[2:], string)
            else:
                return False
        else:
            # print("uFalse")  # Debug
            return False


def find_pattern(re, long_str):
    """Finds the regex pattern inside a longer string"""
    if match_string(re, long_str):
        # 're' pattern WAS found inside long_str or a slice of long_str
        return True
    else:
        if len(long_str) == 0:
            # long_str was sliced to the end and the 're' pattern
            # WASN'T found inside
            # print("long_str was consumed")  # Debug
            return False
        else:
            # It keeps looking the pattern recursively inside long_str
            # but with an incremented starting position
            return find_pattern(re, long_str[1:])


def main_func():

    regex, word = input().split("|")

    if len(regex) > 1 and regex[0] == "^":
        # Non-empty regex was provided and it starts with "^" special
        # character that points the patter must be located at the
        # beggining of the string, this is why check_string() is
        # called directly. (We don't need to look for it in a
        # longer srting)
        print(match_string(regex[1:], word))
    else:
        print(find_pattern(regex, word))


if __name__ == '__main__':
    global plus_flag
    plus_flag = False
    main_func()
