def trisect(f, a, b, n):
    for i in range(n):
        x1 = a + (b - a)/4
        x2 = a + 2 * (b - a)/4
        x3 = a + 3 * (b - a)/4
        xs = [x1, x2, x3]
        min_x_index = 0
        for j in range(len(xs)):
            if f(xs[j]) < f(xs[min_x_index]):
                min_x_index = j
        if min_x_index == 0:
            a = a
            b = x2
        elif min_x_index == 1:
            a = x1
            b = x3
        elif min_x_index == 2:
            a = x2
            b = b
    return (a + b) / 2


def test():
    def f(x):
        return (x - 5) ** 2
    print(trisect(f, 0, 10, 5))

if __name__ == "__main__":
    test()
