def dichotomy(F, a, b, epsilon):
    """
    二分法查找一维最小值
    """
    f = {} # 用一个字典记录已经计算的函数值，再次需要这个函数值的时候直接从字典调用，不重新计算
    val_num = len(str(epsilon).split(".")[1])
    i = 0
    print("Round 1:")
    print("a0:", a)
    print("b0:", b)
    while round(b - a, val_num) > epsilon:
        a0 = a
        b0 = b
        c = (b + a)/2
        x_1 = c - epsilon/2
        x_2 = c + epsilon/2
        print("x1: ", x_1)
        print("x2: ", x_2)
        print("F(x1): ", F(x_1, f, val_num))
        print("F(x2): ", F(x_2, f, val_num))
        if F(x_1, f, val_num) > F(x_2, f, val_num):
            a = x_1
            b = b
            print("F(x1) is bigger than F(x2)")
        else:
            a = a
            b = x_2
            print("F(x1) is smaller than  or eaqual to F(x2)")
        print("-" * 100)
        print("Round %d" %(i + 2))
        print("a%d: "%(i + 1), a)
        print("b%d: "%(i + 1), b)
        i += 1
    return round((a+b)/2, val_num)

def F(x, f, val_num):
    if round(x, val_num) not in f.keys():
        f[round(x, val_num)] = (x - 5) ** 2
    return f[round(x, val_num)]

def test():
    print(dichotomy(F, 0, 10, 0.0001))

if __name__ == "__main__":
    test()
