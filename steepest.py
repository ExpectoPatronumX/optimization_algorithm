import numpy as np
import sympy as sp
from newton import newton
import math
def steepest(F, x1, x2, x_0):
    f = []
    g_num = []
    p = []
    g = np.array([[sp.diff(F, x1)], [sp.diff(F, x2)]])
    t = sp.symbols("t")
    t_num = []
    x = []
    x_num = []
    x.append(x_0)
    x_num.append(x_0)
    g_num.append(np.array([[g[0][0].evalf(subs={"x1":x_0[0][0], "x2":x_0[1][0]})], 
                           [g[1][0].evalf(subs={"x1":x_0[0][0], "x2":x_0[1][0]})]
                          ]))
    i = 0
    while i == 0 or round(math.sqrt(g_num[i][0][0] ** 2 + g_num[i][1][0] ** 2), 4) >= 0.001:
        p.append(-g_num[i])
        print("g%d:\n"%(i), g_num[i])
        print("p%d:\n"%(i), p[i])
        print("x%d:\n"%(i), x_num[i])
        x.append(x_num[i] + t * p[i])
        print("x%d:\n"%(i + 1), x[i + 1])
        f.append(F.evalf(subs = {"x1":x[i + 1][0][0], "x2":x[i + 1][1][0]}))
        print("f(t):\n", f[i])
        t_num.append(newton(f[i], t, 1, 0.001))
        print("t%d:\n"%(i), t_num[i])
        x_num.append(np.array([[x[i + 1][0][0].evalf(subs={"t":t_num[i]})], 
                               [x[i + 1][1][0].evalf(subs={"t":t_num[i]})]
                               ]))
        print("x%d:\n"%(i + 1), x_num[i + 1])
        g_num.append(np.array([[g[0][0].evalf(subs={"x1":x_num[i][0][0], "x2":x_num[i][1][0]})], 
                               [g[1][0].evalf(subs={"x1":x_num[i][0][0], "x2":x_num[i][1][0]})]
                              ]))
        print(math.sqrt(g_num[i + 1][0][0] ** 2 + g_num[i + 1][1][0] ** 2))
        i += 1

def test():
    x1 = sp.symbols("x1")
    x2 = sp.symbols("x2")
    F = x1 ** 2 + x2 ** 2
    x_0 = np.array([[4], [3]])
    steepest(F, x1, x2, x_0)

if __name__ == "__main__":
    test()
