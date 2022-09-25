def F(x, f):
    if x not in f.keys():
        f[x]  = x**2
        print("%d not in f" % (x))
    return f[x]

def test():
    f = {}
    print(F(3, f))
    print(F(3, f))
    print(F(4, f))
    print(f)

if __name__ == "__main__":
    test()
