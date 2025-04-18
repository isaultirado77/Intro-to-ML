#!/usr/bin/env python3

import numpy as np
import scipy.linalg as linalg

def vector_lengths(a: np.ndarray) -> np.ndarray:
    return np.sqrt(np.sum(a**2, axis=1))

def main():
    vector = np.array([-1, 2, 2])
    print("func", vector_lengths(vector))

if __name__ == "__main__":
    main()
