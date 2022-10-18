import numpy as np

def get_grade(f, X):
    return np.gradient(f, X)

def f(X):
    return X[0][0] + X[1][0]

def test():
    X = np.array([[1], [1]])
    print(get_grade(f, X))

if __name__ == "__main__":
    test()
