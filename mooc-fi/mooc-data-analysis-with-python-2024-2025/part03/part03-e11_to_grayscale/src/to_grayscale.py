#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def to_grayscale(img: np.ndarray):
    gray = img[:, :, 0] * 0.2126 + img[:, :, 1] * 0.7152 + img[:, :, 2] * 0.0722
    return gray


def to_red(img: np.ndarray):
    m, n, _ = img.shape
    zeros = np.zeros((m, n))
    red = img[:, :, 0]
    return np.stack([red, zeros, zeros], axis=-1)


def to_green(img: np.ndarray):
    m, n, _ = img.shape
    zeros = np.zeros((m, n))
    green = img[:, :, 1]
    return np.stack([zeros, green, zeros], axis=-1)


def to_blue(img: np.ndarray):
    m, n, _ = img.shape
    zeros = np.zeros((m, n))
    blue = img[:, :, 2]
    return np.stack([zeros, zeros, blue], axis=-1)


def main():
    parent_path = Path(__file__).parent
    image_path = parent_path / "painting.png"
    image = plt.imread(image_path)

    gray = to_grayscale(image)

    red = to_red(image)
    green = to_green(image)
    blue = to_blue(image)

    fig, axs = plt.subplots(1, 4, figsize=(16, 4))
    axs[0].imshow(image)
    axs[0].set_title("Original")
    axs[1].imshow(gray, cmap="gray")
    axs[1].set_title("Grayscale")
    axs[2].imshow(red)
    axs[2].set_title("Red Channel")
    axs[3].imshow(green)
    axs[3].set_title("Green Channel")

    for ax in axs:
        ax.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
