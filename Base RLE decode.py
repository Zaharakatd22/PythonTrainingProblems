import re


seq: list = list(filter(lambda x: x != '', re.split(r'(\d*)(\w)', input())))


def gen(s):
    for elem in s:
        yield elem


a = gen(seq)
for elm in a:
    if elm.isdigit():
        print(next(a) * int(elm), end='')
    else:
        print(elm, end='')
