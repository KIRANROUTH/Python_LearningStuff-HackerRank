#Question Link: https://www.algoexpert.io/questions/Nth%20Fibonacci
def getNthFib(n):
    a, b = 0, 1
    c = a + b
    for _ in range(2, n - 1):
        a = b
        b = c
        c = a + b
    if n == 0 or n == 1:
        print(int(0))
    elif n == 2 or n == 3:
        print(int(1))
    else:
        print(c)

getNthFib(5)
