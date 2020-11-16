# A debuged version of this script is provided by solved_debuged.py

def match_char(re, char):
    """Compares single characters. Taking into account the '.'
    wildcard"""
    return re == '' or char == re or (re == '.' and char != '')


def match_string(re, string):
    """Compares strings of the same length. Handles also special
    characters as '?', '*' or '+'"""
    if re == '' or (re == '$' and string == ''):
        return True
    elif string == '':
        return False
    elif len(re) > 1 and re[1] in '*?+':
        if re[1] in '?*' and match_string(re[2:], string):
            return True
        # Here is the most important part, where is using the
        # recursion to call itself **inside the condition!!**
        elif match_char(re[0], string[0]) and \
                ((re[1] in '?+' and match_string(re[2:], string[1:])) or
                    (re[1] in '*+' and match_string(re, string[1:]))):
            return True
    elif not match_char(re[0], string[0]):
        return False

    return match_string(re[1:], string[1:])


def find_match(re, long_string):
    """Looks for matches in a longer string (than the regex)"""
    if re == '':
        return True
    if re[0] == '^':
        return match_string(re[1:], long_string)

    if match_string(re, long_string):
        return True
    elif long_string:
        return find_match(re, long_string[1:])
    else:
        return False


def main_func():
    """Main function to acquire the input strings"""
    print(find_match(*input().split('|')))


if __name__ == "__main__":
    main_func()
