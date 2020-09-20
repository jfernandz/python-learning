def input_starting_with_regex(reg, inp):
    if not reg or reg == "$" and not inp:
        return True

    if not inp or reg[0] not in (".", inp[0]):
        if len(reg) > 1 and (reg[1] == "?" or reg[1] == "*"):
            return input_starting_with_regex(reg[2:], inp)
        return False

    if len(reg) >= 2:
        if reg[1] == "+":
            return input_starting_with_regex(reg.replace("+", "*", 1), inp[1:])
        if reg[1] == "?":
            return input_starting_with_regex(reg[2:], inp) \
                or input_starting_with_regex(reg[2:], inp[1:])
        if reg[1] == "*":
            return input_starting_with_regex(reg[2:], inp) \
                or input_starting_with_regex(reg, inp[1:])

    return input_starting_with_regex(reg[1:], inp[1:])


def apply_regex(reg, inp):
    if len(reg) > 0 and reg[0] == "^":
        return input_starting_with_regex(reg[1:], inp)
    else:
        return input_starting_with_regex(reg, inp) \
            or bool(inp) and apply_regex(reg, inp[1:])


regex, input_ = input().split('|')

print(apply_regex(regex, input_))
