import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from time import perf_counter
from graham_scan import graham_scan
from fib_heap import fib_sort_points
from merge_sort import merge_sort

matplotlib.use('agg')


if __name__ == '__main__':
    max_size = 1000
    n_iter = 100
    total_fib = []
    total_merge = []
    for n in tqdm(range(1, max_size)):
        time_fib = []
        time_merge = []
        for _ in range(n_iter):
            points = np.random.random((n, 2))
            
            start_point = min(points, key=lambda p: (p[1], p[0]))
            for i, val in enumerate(points):
                if np.all(val == start_point):
                    break
            points = np.delete(points, [i], axis=0)
            
            start = perf_counter()
            sorted_points = fib_sort_points(points, start_point)
            end = perf_counter()
            time_fib.append(end - start)
            
            start = perf_counter()
            sorted_points = merge_sort(points, start_point)
            end = perf_counter()
            time_merge.append(end - start)
            
        total_fib.append(sum(time_fib) / n_iter)
        total_merge.append(sum(time_merge) / n_iter)
        
    plt.plot(range(1, max_size), total_merge, color="red", label='merge')
    plt.plot(range(1, max_size), total_fib, color="green", label='fibonacci')
    plt.xlabel("Number of points")
    plt.ylabel("Time (sec.)")
    plt.legend()
    plt.savefig("vis/sorting_time.jpg")
            
            