import numpy as np
from graham_scan import graham_scan
from scipy.spatial import ConvexHull
from tqdm import tqdm


if __name__ == "__main__":
    n = 1000
    for _ in tqdm(range(100)):
        points = np.random.random((n, 2))

        true_points = ConvexHull(points)
        true_points = sorted(points[true_points.vertices].tolist(), key=lambda p: (p[0], p[1]))

        my_points = sorted(graham_scan(points).tolist(), key=lambda p: (p[0], p[1]))

        if true_points != my_points:
            print(points)
            exit()

    print("All good")

    