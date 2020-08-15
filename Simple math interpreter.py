a, operator, b = input().split()
a, b = int(a), int(b)

if operator == 'plus':
    print(a + b)
elif operator == 'minus':
    print(a - b)
elif operator == 'multiply':
    print(a * b)
elif operator == 'divide':
    print(a // b)
else:
    print(None)
