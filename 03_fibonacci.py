def fibonacci(f, a_0, b_0, n, epsilon):
    f = {}
    #val_num = len(str(epsilon).split(".")[1])
    val_num = 3
    x1 = [a_0]
    x2 = [b_0]
    L_1 = b_0 - a_0
    L_2 = (Fib(n - 1) * L_1) / (Fib(n)) + (((-1) ** n) * epsilon) / (Fib(n))
    b = [a_0 + L_2]
    a = [b_0 - L_2]
    flag = -1
    if F(a[0], f, val_num) < F(b[0], f, val_num):
        x1.append(x1[0])
        x2.append(b[0])
        flag = 0
    else:
        x1.append(a[0])
        x2.append(x2[0])
        flag = 1
    for i in range(1, n):
        if flag == 0:
            b.append(a[i - 1])
            a.append(x2[i] - (b[i] - x1[i]))
            if F(a[i], f, val_num) < F(b[i], f, val_num):
                x1.append(x1[i])
                x2.append(b[i])
                flag = 0
            else:
                x1.append(a[i])
                x2.append(x2[i])
                flag = 1
        elif flag == 1:
            a.append(b[i - 1])
            b.append(x1[i] + (x2[i] - a[i]))
            if F(a[i], f, val_num) < F(b[i], f, val_num):
                x1.append(x1[i])
                x2.append(b[i])
                flag = 0
            else:
                x1.append(a[i])
                x2.append(x2[i])
                flag = 1
    return (x1[-1] + x2[-1]) / 2


def Fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return Fib(n - 1) + Fib(n - 2)

def F(x, f, val_num):
    if round(x, val_num) not in f:
        f[round(x, val_num)] = (x - 5) ** 2
    return f[round(x, val_num)]

def test():
    print(fibonacci(F, 0, 10, 10, 0))

if __name__ == "__main__":
    test()
