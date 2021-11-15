def func(n):
    if n <= 9:
        return 1
    return func(n / 10) + 1

print(func(100))
