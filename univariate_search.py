import numpy as np
import sympy as sp
import math
from newton import newton

def univariate_search(f, x_0):
    t = sp.symbols("t")
    t_1 = []
    t_2 = []
    e1 = np.array([[1], 
                   [0]])
    e2 = np.array([[0], 
                   [1]])
    x0 = []
    x1 = []
    x2 = []
    x0.append(x_0)
    f1 = []
    f2 = []
    i = 0
    print("-" * 100)
    while (i == 0 or math.sqrt((x0[i] - x0[i - 1])[0][0] ** 2 
                             + (x0[i] - x0[i - 1])[1][0] ** 2) >= 0.001):
        print("Round%d" % (i + 1))
        x1.append(x0[i] + t * e1)
        print("x1:\n", x1[i])
        f1.append(f(x1[i]))
        print("f:\n", f1[i])
        t_1.append(newton(f1[i], t, 0, 0.001))
        print("t1:\n", t_1[i])
        x1[i][0][0] = x1[i][0][0].evalf(subs={"t":t_1[i]}) 
        x1[i][1][0] = x1[i][1][0].evalf(subs={"t":t_1[i]}) 
        print("x1:\n", x1[i])
        x2.append(x1[i] + t * e2)
        print("x2:\n", x2[i])
        f2.append(f(x2[i]))
        print("f:\n", f2[i])
        t_2.append(newton(f2[i], t, 0, 0.001))
        print("t2:\n", t_2[i])
        x2[i][0][0] = x2[i][0][0].evalf(subs={"t":t_2[i]}) 
        x2[i][1][0] = x2[i][1][0].evalf(subs={"t":t_2[i]}) 
        print("x2:\n", x2[i])
        x0.append(x2[i])
        print("-" * 100)
        i += 1

def test():
    x_0 = np.array([[1], 
                    [2]])
    univariate_search(f, x_0)
    # print(x)

def f(x):
    return x[0][0] ** 2 + 4 * x[1][0] ** 2

if __name__ == "__main__":
    test()
