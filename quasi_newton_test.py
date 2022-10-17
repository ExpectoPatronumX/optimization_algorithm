import numpy as np
import sympy as sp
import math

def quasi_newton(f, x0):
    i = 0
    x = []
    H = []
    x_num = []
    gs = []
    ts = []
    t = sp.symbols("t")
    t_num = []
    p = []
    delta_x = []
    delta_g = []
    while i == 0 or math.sqrt(g(x_num[i])[0][0] ** 2 + g(x_num[i])[1][0] ** 2) >= 0.01:
        if i == 0:
            print("Roud %d"%(i + 1))
            H.append(np.array([[1, 0],[0, 1]]))
            print("H%d:\n"%(i),np.around( H[i], 6))
            x_num.append(np.array(x0))
            x.append(np.array(x0))
            print("x0:\n", np.around(x_num[i], 6))
            gs.append(g(x_num[i]))
            p.append(-gs[i])
            print("g0:\n", np.around(gs[i], 6))
            print("p0:\n", np.around(p[i], 6))
            x.append(x[i] + t * p[0])
            print("x%d:\n"%(i + 1), x[i+1])
            print("f(x%d):\n"%(i + 1), f(x[i+1]))
            print("f'(t):\n", sp.diff(f(x[i+1]), t))
            t_num.append(np.array(sp.solve(sp.diff(f(x[i+1]), t), t)))
            print(type(t_num[i]))
            print(t_num[i])
            print("t0:\n", t_num[i])
            x_num.append(x[i] + t_num[i] * p[i])
            print("x1:\n", x_num[i+1])
            #gs.append(g(x_num[i+1]))
            print("-" * 100)
        else:
            print("Roud %d"%(i + 1))
            gs.append(g(x_num[i]))
            delta_x.append(x_num[i] - x_num[i - 1])
            delta_g.append(gs[i] - gs[i - 1])
            add1 = delta_x[i - 1] @ delta_x[i - 1].T / (delta_x[i - 1].T @ delta_g[i - 1])
            add2 = (H[i - 1] @ delta_g[i - 1] @ delta_g[i - 1].T @ H[i - 1] / 
                    (delta_g[i - 1].T @ H[i - 1] @ delta_g[i - 1]))
            H.append(H[i - 1] + add1 - add2)
            print("H%d:\n"%(i), H[i])
            p.append(- H[i] @ gs[i])
            print("p%d:\n"%(i), p[i])
            x.append(x_num[i] + t * p[i])
            print("x%d:\n"%(i + 1), x[i + 1])
            t_num.append(sp.solve(sp.diff(f(x[i + 1]), t), t))
            print("t%d:\n"%(i + 1), t_num[i])
            x_num.append(x_num[i] + t_num[i] *  p[i])
            print("x%d:\n"%(i + 1), x_num[i + 1])
            print("-" * 100)
        i += 1

    # The second round
#    delta_x_0 = x_1_num - x_0
#    delta_g_0 = g_1 - g_0
#    print("delta_x_0\n", delta_x_0)
#    print("delta_g_0\n", delta_g_0)
#    H_0 = np.array([[1,0], [0, 1]])
#    print(delta_x_0 @ delta_x_0.T)
#    print(delta_x_0.T @ delta_g_0)
#    add1 = delta_x_0 @ delta_x_0.T / (delta_x_0.T @ delta_g_0)
#    print(add1)
#    add2 = (H_0 @ delta_g_0 @ delta_g_0.T @ H_0) / delta_g_0.T @ H_0 @ delta_g_0
#    print(add2)
#    H_1 = H_0 + add1 - add2
#    print(H_1)
#    p_1 = - H_1 @ g_1
#    print(p_1)
#    x_2 = x_1_num + t * p_1
#    print(x_2)
#    t_num = sp.solve(sp.diff(f(x_2), t), t)
#    print(sp.diff(f(x_2), t))
#    print(t_num)
#    x_2_num = x_1_num + t_num * p_1
#    print(x_2_num)




def f(X):
    return X[0][0] ** 2 + 4 * X[1][0] ** 2

def g(X):
    return np.array([[2 * X[0][0]] , [8 * X[1][0]]])

if __name__ == "__main__":
    quasi_newton(f, [[1], [1]])

