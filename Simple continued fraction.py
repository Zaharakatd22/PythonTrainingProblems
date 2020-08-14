dividend, divisor = map(int, input().split('/'))
continued_fraction: list = []
while divisor != 0:
    continued_fraction.append(str(dividend // divisor))
    dividend, divisor = divisor, dividend % divisor

print(' '.join(continued_fraction))
