import sympy as sp
def newton(F, x, x_0, epsilon):
    f = []
    F_x = []
    F_xx = []
    xs = [x_0]
    i = 0
    while i == 0 or F_x[-1] > epsilon :
        #print("Round %d" %(i + 1))
        F_x.append(sp.diff(F, x).evalf(subs = {x: xs[i]}))
        F_xx.append(sp.diff(F, x, 2).evalf(subs = {x: xs[i]}))
        #print("F'(x%d):"%(i), F_x[i])
        #print("F''(x%d):"%(i), F_xx[i])
        xs.append(xs[i] - F_x[i] / F_xx[i])
        #print("x%d:"%(i + 1), xs[i + 1])
        #print("-" * 100)
        i += 1
    return xs[-1]
def test():
    x = sp.symbols("x")
    F = (x - 5) ** 2
    print(newton(F, x, 7, 0.001))


if __name__ == "__main__":
    test()
