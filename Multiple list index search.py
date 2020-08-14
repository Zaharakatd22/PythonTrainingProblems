lst: list = input().split()
num: str = input()
is_nan: bool = True

for i, elm in enumerate(lst):
    if elm == num:
        print(i, end=' ')
        is_nan = False

if is_nan:
    print(None)
