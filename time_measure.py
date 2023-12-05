import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from time import perf_counter
from graham_scan import graham_scan

matplotlib.use('agg')


def time_measure(mode, n_points=100, n_iter=100):    
    total_time = []
    for n in tqdm(range(3, n_points)):
        time = []
        for _ in range(n_iter):
            points = np.random.random((n, 2))
            start = perf_counter()
            graham_scan(points, mode, vis=False)
            end = perf_counter()
            time.append(end - start)
        total_time.append(sum(time) / n_iter)
        
    return total_time

if __name__ == '__main__':
    n_points = 1000
    n_inter = 100
    
    time_merge = time_measure("merge", n_points, n_inter)
    time_fib = time_measure("fib", n_points, n_inter)
        
    plt.plot(range(3, n_points), time_fib, color="red", label='fibonacci')
    plt.plot(range(3, n_points), time_merge, color="green", label='merge')
    plt.xlabel("Number of points")
    plt.ylabel("Time (sec.)")
    plt.legend()
    
    plt.savefig("vis/time.jpg")
    
        