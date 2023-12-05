import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import dot
from numpy.linalg import norm


def random_points():
    print("Number of points:", end=" ")
    n = int(input())
    points = np.random.random((n, 2))

    return points


def user_points():
    print("Number of points:", end=" ")
    n = int(input())
    points = np.zeros((n, 2))
    for i in range(n):
        print(f"x{i} = ", end="")
        x = float(input())

        print(f"y{i} = ", end="")
        y = float(input())

        points[i][0] = x
        points[i][1] = y

    return points


def cos(p1, p2):
    return dot(p1, p2)/(norm(p1)*norm(p2))


def orientation(a, b, c):
    val = (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

    if val == 0:
        return 0
    
    return 1 if val > 0 else -1