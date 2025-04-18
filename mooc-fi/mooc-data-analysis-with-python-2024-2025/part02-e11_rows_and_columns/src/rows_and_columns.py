#!/usr/bin/env python3

import numpy as np

def get_rows(a: np.ndarray):
    return [a[i] for i in range(len(a))]

def get_columns(a: np.ndarray):
    return get_rows(a.T)

def main():
    np.random.seed(0)
    a = np.random.randint(low=0,high=10, size=(4,4))
    print("a:\n", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
