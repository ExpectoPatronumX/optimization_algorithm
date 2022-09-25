def F(x, f):
    if x not in f.keys():
        f[x] = 3*x**2
        print("%f not in f!" % (x))
    return f[x]

if __name__ == "__main__":
    f = {}
    print(F(3, f))
    print(F(3, f))
    print(F(4, f))
