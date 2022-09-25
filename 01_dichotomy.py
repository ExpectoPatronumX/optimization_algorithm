def dichotomy(F, a, b, epsilon):
    """
    二分法查找一维最小值
    """
    f = {}
    val_num = len(str(epsilon).split(".")[1])
    while round(b - a, val_num) > epsilon:
        a0 = a
        b0 = b
        c = (b + a)/2
        x_1 = c - epsilon/2
        x_2 = c + epsilon/2
        if F(x_1, f, val_num) > F(x_2, f, val_num):
            a = x_1
            b = b
        else:
            a = a
            b = x_2
    return round((a+b)/2, val_num)

def F(x, f, val_num):
    if round(x, val_num) not in f.keys():
        f[round(x, val_num)] = (x - 5) ** 2
    return f[round(x, val_num)]

def test():
    print(dichotomy(F, 0, 10, 0.0001))

if __name__ == "__main__":
    test()
