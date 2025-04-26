#!/usr/bin/env python3

import numpy as np

def diamond(n):
    size = 2 * n - 1
    result = np.zeros((size, size), dtype=int)
    # Parte superior e inferior del diamante
    for i in range(n):
        result[i, n - 1 - i] = 1
        result[i, n - 1 + i] = 1
        result[size - 1 - i, n - 1 - i] = 1
        result[size - 1 - i, n - 1 + i] = 1

    return result

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()
