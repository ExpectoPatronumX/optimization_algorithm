import numpy as np
import sympy as sp
import math
from newton import newton

def conjugate_gradient(F, x1, x2, x0, epsilon):
    g = np.array([[sp.diff(F, x1)], 
                  [sp.diff(F, x2)]])
    t = sp.symbols("t")
    p = []
    t_num = []
    alpha = []
    f = []
    x = []
    x_num = []
    x.append(x0)
    x_num.append(x0)
    gs = []
    gs.append(np.array([[g[0][0].evalf(subs = {"x1":x[0][0][0], "x2":x[0][1][0]})], 
                        [g[1][0].evalf(subs = {"x1":x[0][0][0], "x2":x[0][1][0]})]
                       ]))
    print("F:\n", F)
    print("g:\n", g)
    print("x0:\n", x[0])
    print("-" * 100)
    i = 0
    while i == 0 or round(math.sqrt(gs[i][0][0] ** 2 + gs[i][1][0] ** 2)) >= epsilon:
        if i == 0 :
            print("Round1")
            p.append(-gs[i])
            x.append(x_num[i] + t * p[i])
            f.append(F.evalf(subs = {"x1":x[i + 1][0][0], "x2":x[i + 1][1][0]}))
            t_num.append(newton(f[i], t, 1, 0.001))
            x_num.append(np.array([[x[i + 1][0][0].evalf(subs={"t":t_num[i]})],
                                   [x[i + 1][1][0].evalf(subs={"t":t_num[i]})]
                                  ]))
            gs.append(np.array([[g[0][0].evalf(subs={"x1":x_num[i + 1][0][0], "x2":x_num[i + 1][1][0]})],
                                   [g[1][0].evalf(subs={"x1":x_num[i + 1][0][0], "x2":x_num[i + 1][1][0]})]
                             ]))
            print("g%d:\n"%(i), gs[i])
            print("p%d:\n"%(i), p[i])
            print("x%d:\n"%(i + 1), x[i + 1])
            print("f%d:\n"%(i), f[i])
            print("t%d:\n"%(i), t_num[i])
            print("x%d:\n"%(i + 1), x_num[i + 1])
            print("-" * 100)
        else:
            print("Round%d" % (i + 1))
            alpha.append((gs[i][0][0] ** 2 + gs[i][1][0] ** 2)
                       / (gs[i - 1][0][0] ** 2 + gs[i - 1][1][0] ** 2))
            print("g%d:\n"%(i), gs[i])
            print("alpha%d:\n" % (i - 1), alpha[i - 1])
            p.append(-gs[i] + alpha[i - 1] *  p[i - 1])
            x.append(x_num[i] + t * p[i])
            f.append(F.evalf(subs = {"x1":x[i + 1][0][0], "x2":x[i + 1][1][0]}))
            t_num.append(newton(f[i], t, 1, 0.001))
            x_num.append(np.array([[x[i + 1][0][0].evalf(subs={"t":t_num[i]})],
                                   [x[i + 1][1][0].evalf(subs={"t":t_num[i]})]
                                  ]))
            gs.append(np.array([[g[0][0].evalf(subs={"x1":x_num[i + 1][0][0], "x2":x_num[i + 1][1][0]})],
                                   [g[1][0].evalf(subs={"x1":x_num[i + 1][0][0], "x2":x_num[i + 1][1][0]})]
                             ]))
            print("p%d:\n"%(i), p[i])
            print("x%d:\n"%(i + 1), x[i + 1])
            print("f%d:\n"%(i), f[i])
            print("t%d:\n"%(i), t_num[i])
            print("x%d:\n"%(i + 1), x_num[i + 1])
            print("-" * 100)
        i += 1

def test():
    x1 = sp.symbols("x1")
    x2 = sp.symbols("x2")
    F = x1 **2 + 25 * x2 ** 2
    x0 = np.array([[2], 
                   [2]])
    conjugate_gradient(F, x1, x2, x0, 0.01)

if __name__ == "__main__":
    test()
