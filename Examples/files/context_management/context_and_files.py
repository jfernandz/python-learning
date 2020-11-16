# `with ... as:` statement is intended to manage resources, when
# you work with files, for example, is an interesting way to avoid
# the .close() method, as the following lines show, you can open
# several files, work with them and you don't need to close, because
# `with ... as:` statement is doing it for you.


for i in range(1, 3):
    with open(f'file{i}.txt', 'w') as f:
        f.write(f"file number {i}")
