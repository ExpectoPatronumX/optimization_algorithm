def quadratic_interpolation(F, a, b, epsilon):
    f = {}
    val_num = len(str(epsilon).split(".")[1])
    x1 = [a]
    x3 = [b]
    x2 = []
    xp = []
    f1 = []
    f2 = []
    f3 = []
    fp = []
    i = 0
    while i == 0 or i == 1 or abs(xp[-2] - xp[-1]) > epsilon:
        print("Round %d" % (i + 1))
        x2.append((x1[i] + x3[i]) / 2)
        f1.append(F(x1[i], f, val_num))
        f2.append(F(x2[i], f, val_num))
        f3.append(F(x3[i], f, val_num))
        print("x1:", x1[i])
        print("x2:", x2[i])
        print("x3:", x3[i])
        print("f1:", f1[i])
        print("f2:", f2[i])
        print("f3:", f3[i])
        xp.append((1 / 2) 
                * ((x2[i] ** 2 - x3[i] ** 2) * (f1[i]) 
                    + (x3[i] ** 2 - x1[i] ** 2) * (f2[i]) 
                    + (x1[i] ** 2 - x2[i] ** 2) * (f3[i])) 
                / ((x2[i] - x3[i]) * (f1[i]) 
                    + (x3[i] - x1[i]) * (f2[i]) 
                    + (x1[i] - x2[i]) * (f3[i])))
        fp.append(F(xp[i], f, val_num))
        print("xp:", xp[i])
        print("fp:", fp[i])
        if x2[i] < xp[i]:
            print("xp is bigger than x2")
            if f2[i] < fp[i]:
                x1.append(x1[i])
                x3.append(xp[i])
                print("fp is bigger than f2")
            else:
                x1.append(x2[i])
                x3.append(x3[i])
                print("fp is smaller than or equal to f2")
        else:
            print("xp is smaller than or equal to x2")
            if f2[i] < fp[i]:
                x1.append(xp[i])
                x3.append(x3[i])
                print("fp is bigger than f2")
            else:
                x1.append(x1[i])
                x3.append(x2[i])
                print("fp is smaller than or equal to f2")
        print("-" * 100)
        i += 1
    return xp[-1]

def test():
    print(quadratic_interpolation(F, 0, 10, 0.001))

def F(x, f, val_num):
    if round(x, val_num) not in f.keys():
        f[round(x, val_num)] = (x - 5) ** 2
    return f[round(x, val_num)]

if __name__ == "__main__":
    test()
