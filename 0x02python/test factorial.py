def factorial(n):
    n = 20
    if (n == 0 or n== 1):
        return 1
    return n * factorial(n - 1)
print(factorial)