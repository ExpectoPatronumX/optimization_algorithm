import sympy as sp
import numpy as np
def newton(F, x, x_0, epsilon):
    f = []
    F_x = []
    F_xx = []
    xs = [x_0]
    i = 0
    while i == 0 or F_x[-1] > epsilon :
        F_x.append(sp.diff(F, x).evalf(subs = {x: xs[i]}))
        F_xx.append(sp.diff(F, x, 2).evalf(subs = {x: xs[i]}))
        xs.append(xs[i] - F_x[i] / F_xx[i])
        i += 1
    return xs[-1]
def test():
    x = sp.symbols("x")
    F = (x - 5) ** 2
    print(newton(F, x, 4, 0.001))

#def F(x):
#    return "(x - 5) ** 2"

if __name__ == "__main__":
    test()
