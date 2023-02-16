def summa(*args):
    print(args)
    return 0
def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n -1)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

for i in range(100):
    print(i, fib(i))
