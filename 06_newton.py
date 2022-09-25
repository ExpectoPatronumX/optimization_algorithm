def newton():
    pass

def test():
    pass

def F(x, f, val_num):
    if round(x, val_num) not in f.keys():
        f[round(x, val_num)] = (x - 5) ** 2
    return f[round(x, val_num)]

if __name__ == "__main__":
    test()
