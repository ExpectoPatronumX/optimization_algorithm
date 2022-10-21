import numpy as np
import sympy as sp
import math
from newton import newton

def quasi_newton(F, x1, x2, x0, epsilon):
    g = np.array([[sp.diff(F, x1)],
                  [sp.diff(F, x2)]])
    h = np.array([[sp.diff(F, x1, x1), sp.diff(F, x1, x2)],
                  [sp.diff(F, x2, x1), sp.diff(F, x2, x2)]])
    print("g:\n", g)
    print("h:\n", h)
    gs = []
    hs = []
    f = []
    p = []
    x = []
    x_num = []
    t = sp.symbols("t")
    t_num = []
    x.append(x0)
    x_num.append(x0)
    hs.append(np.array([[1, 0], 
                        [0, 1]], dtype = "float64"))
    gs.append(np.array([
                      [float(g[0][0].evalf(subs={"x1":x_num[0][0][0], "x2":x_num[0][1][0]}))],
                      [float(g[1][0].evalf(subs={"x1":x_num[0][0][0], "x2":x_num[0][1][0]}))],
                            ]))
    f.append(float(F.evalf(subs={"x1":x[0][0][0], "x2":x[0][1][0]})))
    delta_x = []
    delta_g = []
    i = 0
    while i == 0 or math.sqrt(gs[i][0][0] ** 2 + gs[i][1][0] ** 2) >= 0.001 :
        if i == 0:
            print("Roud %d"%(i + 1))
            p.append(- gs[i])
            x.append(x[i] + t * p[i])
            f.append(F.evalf(subs = {"x1":x[i + 1][0][0], "x2":x[i + 1][1][0]}))
            t_num.append(newton(f[i + 1], t, 1, 0.001))
            x_num.append(np.array([
                [x[i + 1][0][0].evalf(subs = {"t": t_num[i]})],
                [x[i + 1][1][0].evalf(subs = {"t": t_num[i]})]
                ]))
            gs.append(np.array([
                [g[0][0].evalf(subs = {"x1":x_num[i + 1][0][0], "x2":x_num[i + 1][1][0]})],
                [g[1][0].evalf(subs = {"x1":x_num[i + 1][0][0], "x2":x_num[i + 1][1][0]})]
                ]))
            print("x%d:\n"%(i), x_num[i])
            print("g%d:\n"%(i), gs[i])
            print("p%d:\n"%(i), p[i])
            print("x%d:\n"%(i + 1), x[i + 1])
            print("f%d:\n"%(i + 1), f[i + 1])
            print("t%d:\n"%(i), t_num[i])
            print("x%d:\n"%(i + 1), x_num[i + 1])
            print("-" * 100)
        else:
            print("Roud %d"%(i + 1))
            delta_x.append(x_num[i] - x_num[i - 1])
            delta_g.append(gs[i] - gs[i - 1])
            add1 = (delta_x[i - 1] @ delta_x[i - 1].T) / (delta_x[i - 1].T @ delta_g[i - 1])
            add2 = ((hs[i - 1] @ delta_g[i - 1] @ delta_g[i - 1].T @ hs[i - 1]) 
                  / (delta_g[i - 1].T @ hs[i - 1] @ delta_g[i - 1]))
            hs.append(hs[i - 1] + add1 - add2)
            p.append(- hs[i] @ gs[i])
            x.append(x_num[i] + t * p[i])
            f.append(F.evalf(subs = {"x1":x[i + 1][0][0], "x2":x[i + 1][1][0]}))
            t_num.append(newton(f[i + 1], t, 1, 0.001))
            x_num.append(np.array([
                [x[i + 1][0][0].evalf(subs = {"t": t_num[i]})],
                [x[i + 1][1][0].evalf(subs = {"t": t_num[i]})]
                ]))
            gs.append(np.array([
                [g[0][0].evalf(subs = {"x1":x_num[i + 1][0][0], "x2":x_num[i + 1][1][0]})],
                [g[1][0].evalf(subs = {"x1":x_num[i + 1][0][0], "x2":x_num[i + 1][1][0]})]
                ]))
            print("x%d:\n"%(i), x_num[i])
            print("g%d:\n"%(i), gs[i])
            print("p%d:\n"%(i), p[i])
            print("x%d:\n"%(i + 1), x[i + 1])
            print("f%d:\n"%(i + 1), f[i + 1])
            print("t%d:\n"%(i), t_num[i])
            print("x%d:\n"%(i + 1), x_num[i + 1])
            print("-" * 100)
        i += 1

def test():
    x1 = sp.symbols("x1")
    x2 = sp.symbols("x2")
    F = x1 ** 2 + 25 * x2 ** 2
    x0 = np.array([[2], [2]])
    quasi_newton(F, x1, x2, x0, 0.001)

if __name__ == "__main__":
    test()

