from textwrap import dedent


def bad_multiline():
    print("""whatever
    in two lines""")


def multiline():
    print("whatever"
          + "\nin two lines")


def textwrap_multiline():
    """https://docs.python.org/3/library/textwrap.html"""
    print(dedent("""\
    whatever
    in two lines"""))


def pretty_texwrap_multiline():
    print(
        dedent(
            """\
            whatever
            in two lines"""
        )
    )


print()
bad_multiline()

print()
multiline()

print()
textwrap_multiline()

print()
pretty_texwrap_multiline()

print()
print("""whatever
in two lines""")
