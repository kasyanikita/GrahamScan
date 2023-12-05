import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from tools import user_points, random_points, cos, orientation
from merge_sort import merge_sort
from fib_heap import fib_sort_points

matplotlib.use('agg')


def graham_scan(points, mode="fib", vis=True):
    
    if vis:
        plt.scatter(points[:, 0], points[:, 1])
        plt.savefig("vis/input.jpg")
        
    if len(points) <= 3:
        return points

    start_point = min(points, key=lambda p: (p[1], p[0]))
    for i, val in enumerate(points):
        if np.all(val == start_point):
            break
    points = np.delete(points, [i], axis=0)

    if mode == "merge":
        sorted_points = merge_sort(points, start_point)
    elif mode == "fib":
        sorted_points = fib_sort_points(points, start_point)
    else:
        raise ValueError(f"Unknown mode '{mode}'")
    # sorted_points = sorted(points, key=lambda p: cos(p - start_point, np.array([1, 0])), reverse=True)
    
    n = points.shape[0]
    convex_hull = [start_point, sorted_points[0]]
    for i in range(1, n):
        while orientation(convex_hull[-2], convex_hull[-1], sorted_points[i]) == -1:
            convex_hull.pop()
        convex_hull.append(sorted_points[i])

    convex_hull = np.array(convex_hull)
    
    if vis:
        
        for i, (x,y) in enumerate(sorted_points):
            plt.text(x,y,i, ha="center", va="center", fontsize=17)
        plt.savefig("vis/points_order.jpg")
        
        plt.scatter(convex_hull[:, 0], convex_hull[:, 1], color='red')
        plt.savefig("vis/result.jpg")

    return convex_hull


def main():
    print("Choose type of data (1 or 2):\n1. Random\n2. User\nMode: ", end="")
    mode = input()
    if mode == '1':
        points = random_points()
        graham_scan(points)
    elif mode == '2':
        points = user_points()
        graham_scan(points)
    else:
        raise ValueError(f"Not correct choice '{mode}', expect '1' or '2'")


if __name__ == '__main__':
    main()