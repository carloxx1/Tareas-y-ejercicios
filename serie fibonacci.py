def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

for x in range(15):
    print(fib(x))
