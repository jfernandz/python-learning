# IMPORTANT: This solution does not work for
# ^n.*pe$|nope
# though the Jetbrain tests doesn't notice it


# The most important consideration is that you could compare
# re[0] with string[0] using match_char() without directly
# comparing them the way is by comparing re[0] with string[1]
# AND string[0] with string[1] (line 51), of cours you must
# ensure also that len(re) and len(string) are greater than 1

# This is the most important point because "+" operator was
# the most difficult to implement, and this explained way is
# the best way (for me) to stop the slicing when repetition
# is over, and also a good way to handle the "." operator.


# import sys
# sys.setrecursionlimit(10000)


def match_char(single_re, character):
    """Checks if a single character in a string does match
    a single character in a regular expression (taking into
    account also the wild-card '.' character)
    """
    # returns True if single_re == "." and the result of evaluating
    # the expression (single_re == character)
    return True if single_re == "." else single_re == character


def match_string(re, string):
    """Checks if a regexp-string pair does match. Both of them must
    have the same length!!. i.e. It compares the 're' pattern with
    a given 'string' character by character using match_char()
    function.
    """
    print("-"*6 + "> " + f"{re}|{string}")  # Debug
    if not re:
        # re was consumed so this means the re was found in string
        return True
    elif not string and re in "$.*+":
        # String was consumed but re ends with "$", ".", "*" or "+"
        return True
    elif not string:
        # string was consumed but re wasn't so re wasn't found inside string
        return False
    elif len(re) > 1 and re[1] == "?":
        # following character is "?"
        if match_char(re[0], string[0]) is False:
            return match_string(re[2:], string)
        else:
            return match_string(re[2:], string[1:])
    elif len(re) > 1 and re[1] == "*":
        if match_char(re[0], string[0]) is False:
            return match_string(re[2:], string)
        else:
            return match_string(re, string[1:])
    elif len(re) > 1 and len(string) > 1 and re[1] == "+":
        # Here is the important point, he's using string[1] to ensure that
        # re[0] is also the same than string[0] but without doing the
        # explicit match with match_char() because re[0] could be "."
        print("/"*6 + "> " + f"{re[0]}|{string[0]}/{string[1]}")
        if match_char(re[0], string[1]) and match_char(string[0], string[1]):
            return match_string(re, string[1:])
        else:
            return match_string(re[2:], string[1:])
    elif match_char(re[0], string[0]):
        return match_string(re[1:], string[1:])
    else:
        return False


def find_pattern(re, long_str):
    """Finds the regex pattern inside a longer string"""
    if not re:
        return True
    elif not long_str:
        return False
    elif re[0] == "^":
        return match_string(re[1:], long_str)
    elif match_string(re, long_str) is False:
        # 're' pattern WAS found inside long_str or a slice of long_str
        return find_pattern(re, long_str[1:])
    else:
        return True


def main_func():

    regex, word = input().split("|")
    print(find_pattern(regex, word))


if __name__ == '__main__':
    main_func()
