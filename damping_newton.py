import numpy as np
import sympy as sp
from newton import newton
import math

def newton_multi(F, x1, x2, x0, epsilon):
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
    gs.append(np.array([
        [float(g[0][0].evalf(subs={"x1":x_num[0][0][0], "x2":x_num[0][1][0]}))], 
        [float(g[1][0].evalf(subs={"x1":x_num[0][0][0], "x2":x_num[0][1][0]}))], 
        ]))
    f.append(float(F.evalf(subs={"x1":x[0][0][0], "x2":x[0][1][0]})))
    i = 0
    print("-" * 100)
    while i == 0 or round(math.sqrt(gs[i][0][0] ** 2 + gs[i][1][0] ** 2), 4) >= epsilon :
        print("Round%d"%(i + 1))
        gs.append(np.array([
            [float(g[0][0].evalf(subs={"x1":x_num[i][0][0], "x2":x_num[i][1][0]}))], 
            [float(g[1][0].evalf(subs={"x1":x_num[i][0][0], "x2":x_num[i][1][0]}))], 
            ]))
        hs.append(np.array([
            [float(h[0][0].evalf(subs={"x1":x_num[i][0][0], "x2":x_num[i][1][0]})), 
             float(h[0][1].evalf(subs={"x1":x_num[i][0][0], "x2":x_num[i][1][0]}))], 
            [float(h[1][0].evalf(subs={"x1":x_num[i][0][0], "x2":x_num[i][1][0]})), 
             float(h[1][1].evalf(subs={"x1":x_num[i][0][0], "x2":x_num[i][1][0]}))]
            ]))
        p.append(- np.linalg.inv(hs[i]) @ gs[i])
        x.append(x[i] + t * p[i])
        f.append(F.evalf(subs={"x1":x[i + 1][0][0], "x2":x[i + 1][1][0]}))
        t_num.append(newton(f[i + 1], t, 1, 0.001))
        x_num.append(np.array([[x[i + 1][0][0].evalf(subs = {"t": t_num[i]})], 
                               [x[i + 1][1][0].evalf(subs = {"t": t_num[i]})]
                               ]))
        gs.append(np.array([
            [g[0][0].evalf(subs={"x1":x_num[i][0][0], "x2":x_num[i][1][0]})], 
            [g[1][0].evalf(subs={"x1":x_num[i][0][0], "x2":x_num[i][1][0]})], 
            ]))
        print("x%d:\n"%(i), x_num[i])
        print("g%d:\n"%(i), gs[i])
        print("h%d:\n"%(i), hs[i])
        print("h%d.I:\n"%(i), np.linalg.inv(hs[i]))
        print("p%d:\n"%(i), p[i])
        print("x%d:\n"%(i + 1), x[i + 1])
        print("f%d:\n"%(i + 1), f[i + 1])
        print("t%d:\n"%(i), t_num[i])
        print("x%d:\n"%(i + 1), x_num[i + 1])
        print("abs(g):\n", math.sqrt(gs[i + 1][0][0] ** 2 + gs[i + 1][1][0] ** 2))
        print("-" * 100)
        i += 1

def test():
    x1 = sp.symbols("x1")
    x2 = sp.symbols("x2")
    F = 2 * x1 **2 + 4 * x2 ** 2
    x0 = np.array([[3], 
                   [4]])
    newton_multi(F, x1, x2, x0, 0.001)

if __name__ == "__main__":
    test()
