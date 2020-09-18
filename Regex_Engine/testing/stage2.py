def compare_char(single_re, character):
    if single_re in character:
        return True
    elif single_re == ".":
        return True
    else:
        return False


def check_string(re, string):
    if len(re) == 0:
        return True
    elif len(string) == 0:
        return False

    if compare_char(re[0], string[0]):
        return check_string(re[1:], string[1:])
    else:
        return False


regex, word = input().split("|")
print(check_string(regex, word))
