import numpy as np
from tools import orientation
from math import dist


def merge_sort(arr, start_point):
    if len(arr) <= 1:
        return arr
    
    m = len(arr) // 2
    left_arr = arr[:m]
    right_arr = arr[m:]

    lhs = merge_sort(left_arr, start_point)
    rhs = merge_sort(right_arr, start_point)

    return merge(lhs, rhs, start_point)


def merge(a, b, p):
    result = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if orientation(p, a[i], b[j]) == 1:
            result.append(a[i])
            i += 1
        elif orientation(p, a[i], b[j]) == -1:
            result.append(b[j])
            j += 1
        elif dist(p, a[i]) > dist(p, b[j]):
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            i += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return np.array(result)     
