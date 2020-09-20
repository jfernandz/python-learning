def match_char(re, char):
    """Compares single characters. Taking into account the '.'
    wildcard"""
    return re == '' or char == re or (re == '.' and char != '')


def match_string(re, string, d):
    """Compares strings of the same length. Handles also special
    characters as '?', '*' or '+'"""
    if re == '' or (re == '$' and string == ''):
        return True
    elif string == '':
        return False
    elif len(re) > 1 and re[1] in '*?+':
        if d:
            print("match_string()[if]>    "
                  + "Recursive condition for complex if :"
                  + f"   '{re}|{string}'"
                  + f"        special char found -> {re[1]}")  # Debug
        if re[1] in '?*' and match_string(re[2:], string, d):
            return True
        elif match_char(re[0], string[0]) and \
                ((re[1] in '?+' and match_string(re[2:], string[1:], d)) or
                    (re[1] in '*+' and match_string(re, string[1:], d))):
            if d:
                print("match_string()    >    "
                      + "Returning > True < in complex if   :")
            return True
    elif not match_char(re[0], string[0]):
        return False

    if d:
        print("match_string()    >    "
              + "Usual chop when 1st char matched   :"
              + f"   '{re[1:]}|{string[1:]}'")  # Debug
    return match_string(re[1:], string[1:], d)


def find_match(re, long_string, d):
    """Looks for matches in a longer string (then the regex)"""
    if re == '':
        return True

    if re[0] == '^':
        return match_string(re[1:], long_string, d)

    if match_string(re, long_string, d):
        if d:
            print("find_pattern()    >    "
                  + "long_string MATCHED; last > True < :"
                  + f"   '{re}|{long_string}'")  # Debug
        return True
    elif long_string:
        if d:
            print("find_pattern()    >    "
                  + "long_string did NOT match; checking:"
                  + f"   '{re}|{long_string[1:]}'")  # Debug
        return find_match(re, long_string[1:], d)
    else:
        return False


def main_func(debug=True):
    """Main function to acquire the input strings"""
    print(find_match(*input().split('|'), debug))


if __name__ == "__main__":
    main_func()
