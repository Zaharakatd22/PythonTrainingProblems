n: int = int(input())


def f(x):
    c: int = 0
    for i in range(x + 1):
        for _ in range(i):
            yield i
            c += 1
            if c == x:
                return


for num in f(n):
    print(num, end=' ')
