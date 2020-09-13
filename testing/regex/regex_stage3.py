# import sys
# sys.setrecursionlimit(10000)


def compare_char(single_re, character):
    """Checks if a single character in a string
    does match with a single character in a regular expression
    """
    if single_re in character:
        return True
    elif single_re == ".":
        return True
    else:
        return False


def check_string(re, string):
    """Checks if a regexp-string pair does match. Both of them must
    have the same length!!. If regexp length is less than string length,
    it will return True (This means the regexp was found inside string).
    On the other hand, if string length is less than regexp length, it'll
    return False because string will be consumed but regex won't be found
    inside."""
    if len(re) == 0:
        return True
    elif len(string) == 0:
        return False

    if compare_char(re[0], string[0]):
        return check_string(re[1:], string[1:])
    else:
        return False


def find_pattern(re, long_str):
    """Finds the regex pattern inside a longer string"""
    if check_string(re, long_str):
        return True
    else:
        if len(long_str) == 0:
            # long_str was sliced until the end and the 're'
            # pattern was not found inside
            return False
        else:
            return find_pattern(re, long_str[1:])


regex, word = input().split("|")
print(find_pattern(regex, word))
