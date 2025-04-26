#!/usr/bin/env python3

import numpy as np
from functools import reduce

def matrix_power(a: np.ndarray, n: int): 
    m = len(a)
    if n == 0:
        return np.eye(m)
    elif n == -1: 
        return np.linalg.inv(a)
    elif n < 0:
        return matrix_power(np.linalg.inv(a), -n)
    
    return reduce(lambda X, Y: X @ Y, [a] * n, np.eye(m))

def main():
    A = np.array([[2, 0],
              [0, 2]])

    print(matrix_power(A, 3)) 

if __name__ == "__main__":
    main()
