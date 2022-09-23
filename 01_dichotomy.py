import math
def dichotomy(f, a, b, epsilon):
    while b - a > epsilon:
        a0 = a
        b0 = b
        c = (b + a)/2
        x_1 = c - epsilon/2
        x_2 = c + epsilon/2
        if f(x_1) > f(x_2):
            a = x_1
            b = b
        else:
            a = a
            b = x_2
        if b - a == b0 - a0:
            break
    return (a+b)/2

def test():
    def function1(x):
        return math.e**x - 5*x
    print(dichotomy(function1, 1, 2, 0.0000001))

if __name__ == "__main__":
    test()


