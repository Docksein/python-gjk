def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return f(n - 1) + f(n - 2)


print(f(50))

def fib(n):
    a = 0
    b = 1
    c = a + b
