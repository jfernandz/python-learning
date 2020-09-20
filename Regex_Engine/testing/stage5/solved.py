def match_char(re, char):
    return re == '' or char == re or (re == '.' and char != '')


def match_string(re, string):
    if re == '' or (re == '$' and string == ''):
        return True
    if string == '':
        return False
    if len(re) > 1 and re[1] in '*?+':
        if re[1] in '?*' and match_string(re[2:], string):
            return True
        if match_char(re[0], string[0]) and \
                ((re[1] in '?+' and match_string(re[2:], string[1:])) or
                    (re[1] in '*+' and match_string(re, string[1:]))):
            return True
    if not match_char(re[0], string[0]):
        return False
    return match_string(re[1:], string[1:])


def find_match(re, string):
    if re == '':
        return True
    if re[0] == '^':
        return match_string(re[1:], string)

    if match_string(re, string):
        return True
    else:
        return find_match(re, string[1:])


print(find_match(*input().split('|')))
