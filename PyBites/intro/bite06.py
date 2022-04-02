# Intro Bite 06. Strip out vowels and count the number of replacements:

from typing import Tuple, Optional
import re

TEXT = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
VOWELS = 'aeiou'


def strip_vowels(text: Optional[str] = TEXT) -> Tuple[str, int]:
    """Replace all vowels in the input text string by a star
       character (*).
       Return a tuple of (replaced_text, number_of_vowels_found)

       So if this function is called like:
       strip_vowels('hello world')

       ... it would return:
       ('h*ll* w*rld', 3)

       The str/int/Optional/Tuple types in the function definition above are part
       of Python's new type hinting:
       https://docs.python.org/3/library/typing.html"""
    prog = re.compile(f"[{VOWELS}{VOWELS.upper()}]")
    matches = len(prog.findall(text))
    fixed_text = prog.sub("*", text)
    return fixed_text, matches


# Output (don't need this in PyBites web):
print(strip_vowels())

# Extra info:
"""
An intestresting point seems to be that according to the PyBites solution
re module provides a flag to ignore case: ----> from https://docs.python.org/3/library/re.html#re.I

    # once you get into regular expressions you can rewrite this with one line:
    import re
    return re.subn(f'[{VOWELS}]', '*', text, flags=re.I)

Also ... subn(): ----> from https://docs.python.org/3/library/re.html#re.subn

    Perform the same operation as sub(), but return a tuple (new_string, number_of_subs_made)

Which would have been ideal to not have to create the matches object at L21.
"""
