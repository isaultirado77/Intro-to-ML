#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a: np.ndarray):
    _, m = a.shape
    m = m // 2
    mask = np.sum(a[:, :m], axis=1) > np.sum(a[:, m: ], axis=1)
    return a[mask]

def main():
    a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2]])
    print( first_half_second_half(a) )

if __name__ == "__main__":
    main()
