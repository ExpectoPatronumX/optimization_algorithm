def fibonacci(f, a_0, b_0, n, epsilon):
    a = []
    b = []
    a.append(a_0)
    b.append(b_0)
    L_1 = b[0] - a[0]
    L_2 = (fib(n-1) * L_1) / (fib(n)) + ((-1) ** n * epsilon) / (fib(n))
    x_1 = a[0]
    x_2 = b[0]
    b.append(x_1 + L_2)
    a.append(x_2 - L_2)
    for i in range(n):
        if f(a[i + 1]) < f(b[i + 1]):
            a.append(x_1 + x_2 - a[i + 1])
            b.append(a[i + 1])
            x_1 = a[i]
            x_2 = b[i + 1]
        else:
            a.append(b[i + 1])
            b.append(x_2 - b[i + 1] + x_1)
            x_1 = a[i + 1]
            x_2 = b[i]
    return x_2 - x_1

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def test():
    def f(x):
        return x ** 2
    print(fibonacci(f, -1, 1, 10, 0))
    print(fib(3))

if __name__ == "__main__":
    test()
