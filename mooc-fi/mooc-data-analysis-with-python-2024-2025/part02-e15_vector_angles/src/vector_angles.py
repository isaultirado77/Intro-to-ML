#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X: np.ndarray, Y: np.ndarray):
    dot_product = np.sum(X * Y, axis=1)
    norm_X = np.sqrt(np.sum(X ** 2, axis=1))
    norm_Y = np.sqrt(np.sum(X ** 2, axis=1))
    cos_alpha = dot_product / (norm_X * norm_Y)
    cos_alpha_clipped = np.clip(cos_alpha, -1.0, 1.0)
    alpha_rad = np.arccos(cos_alpha_clipped)
    alpha_deg = np.degrees(alpha_rad)
    return alpha_deg


def main():
    X = np.array([[1, 0], [0, 1], [1, 1]])
    Y = np.array([[0, 1], [1, 0], [-1, -1]])

    angles = vector_angles(X, Y)
    print(angles)  # Output: [90., 90., 180.]


if __name__ == "__main__":
    main()
