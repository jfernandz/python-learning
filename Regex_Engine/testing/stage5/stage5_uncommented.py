# import sys
# sys.setrecursionlimit(10000)


def match_char(single_re, character):
    """Checks if a single character in a string does match
    a single character in a regular expression (taking into
    account also the wild-card '.' character)
    """
    if single_re in character:
        return True
    elif single_re == ".":
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
        return True
    elif len(string) == 0:
        if re == "$":
            return True
        return False

    if len(re) > 1 and re[1] == "?":
        return match_string(*question_mark_op(re, string))

    if match_char(re[0], string[0]):
        return match_string(re[1:], string[1:])
    else:
        return False


def question_mark_op(re, string):
    if match_char(re[0], string[0]):
        return re[2:], string[1:]
    else:
        return re[2:], string


def find_pattern(re, long_str):
    """Finds the regex pattern inside a longer string"""
    if match_string(re, long_str):
        return True
    else:
        if len(long_str) == 0:
            return False
        else:
            return find_pattern(re, long_str[1:])


def main_func():

    regex, word = input().split("|")

    if len(regex) != 0 and regex[0] == "^":
        print(match_string(regex[1:], word))
    else:
        print(find_pattern(regex, word))


if __name__ == '__main__':
    main_func()
