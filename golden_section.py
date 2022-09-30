def golden_section(F, a_0, b_0, epsilon):
    f = {}
    val_num = len(str(epsilon).split(".")[1])
    a = [a_0]
    b = [b_0]
    x1 = [a[0] + 0.382 * (b[0] - a[0])]
    x2 = [a[0] + 0.618 * (b[0] - a[0])]
    print("Round 1:")
    print("a:", a[0])
    print("b:", b[0])
    print("x1:", x1[0])
    print("x2:", x2[0])
    print("F(x1):", F(x1[0], f, val_num))
    print("F(x2):", F(x2[0], f, val_num))
    flag = -1
    if F(x1[0], f, val_num) < F(x2[0], f, val_num):
        a.append(a[0])
        b.append(x2[0])
        print("F(x2) is bigger than F(x1)")
        flag = 0
    else:
        a.append(x1[0])
        b.append(b[0])
        print("F(x2) is smaller than  or eaqual to F(x1)")
        flag = 1
    print("-" * 100)
    i = 1
    while round(b[i] - a[i], val_num) > epsilon:
        print("Round %d" %(i + 1))
        if flag == 0:
            x2.append(x1[i - 1])
            x1.append(a[i] + 0.382 * (b[i] - a[i]))
            if F(x1[i], f, val_num) < F(x2[i], f, val_num):
                a.append(a[i])
                b.append(x2[i])
                flag = 0
            else:
                a.append(x1[i])
                b.append(b[i])
                flag = 1
        elif flag == 1:
            x1.append(x2[i - 1])
            x2.append(a[i] + 0.618 * (b[i] - a[i]))
            if F(x1[i], f, val_num) < F(x2[i], f, val_num):
                a.append(a[i])
                b.append(x2[i])
                flag = 0
            else:
                a.append(x1[i])
                b.append(b[i])
                flag = 1
        print("a:", a[i])
        print("b:", b[i])
        print("x1:", x1[i])
        print("x2:", x2[i])
        print("F(x1):", F(x1[i], f, val_num))
        print("F(x2):", F(x2[i], f, val_num))
        if flag == 0:
            print("F(x2) is bigger than F(x1)")
        elif flag == 1:
            print("F(x2) is smaller than  or eaqual to F(x1)")
        print("-" * 100)
        i += 1
    #print(i)
    return (a[-1] + b[-1]) / 2


def test():
    print(golden_section(F, 0, 10, 0.001))

def F(x, f, val_num):
    if round(x, val_num) not in f.keys():
        f[round(x, val_num)] = (x - 5) ** 2
    return f[round(x, val_num)]

if __name__ == "__main__":
    test()
