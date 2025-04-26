#!/usr/bin/env python3

import numpy as np

def get_row_vectors(arr):
    return [row.reshape(1, -1) for row in arr]  # row.reshape(1, -1): remodela row a (1, m), -1 calcula automáticamente el tamaño

def get_column_vectors(arr):
    return [col.reshape(-1, 1) for col in arr.T]  # col.rechape(-1, 1): remodela la columna (de a) a (n, 1) 

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:\n", a)
    print("Row vectors:\n", get_row_vectors(a))
    print("Column vectors:\n", get_column_vectors(a))

if __name__ == "__main__":
    main()
