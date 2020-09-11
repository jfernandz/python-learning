# Single character
#
#
def compare(regexp, character):
    if regexp in character:
        return True
    elif regexp == ".":
        return True
    else:
        return False


reg, exp = input().split("|")


print(compare(reg, exp))


# Strings
#
#
# def compare(regexp, expression):
#     if regexp in expression:
#         return True
#     elif regexp.startswith("."):
#         if regexp[1:] in expression:
#             return True
#     else:
#         return False
#
#
# reg, exp = input().split("|")
#
#
# print(compare(reg, exp))


# Using re module. JetBrains asks me not to use it.
# import re
#
#
# def compare(regexp, expression):
#     if re.search(regexp, expression):
#         return True
#     else:
#         return False
#
#
# reg = input()
# exp = input()
#
# print(compare(reg, exp))
