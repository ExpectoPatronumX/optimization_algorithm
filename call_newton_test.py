from newton import newton
import sympy as sp

def test():
    t = sp.symbols("s")
    F = 3 * t ** 2
    print(newton(F, t, 4, 0.001))

if __name__ == "__main__":
    test()
