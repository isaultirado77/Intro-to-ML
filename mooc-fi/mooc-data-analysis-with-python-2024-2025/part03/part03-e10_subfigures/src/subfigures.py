#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a: np.ndarray):
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Gráfico de línea en el primer eje (izquierda)
    ax[0].plot(a[:, 0], a[:, 1], color='blue')
    ax[0].set_title("Plot")
    ax[0].set_xlabel("X")
    ax[0].set_ylabel("Y")

    # Gráfico de dispersión en el segundo eje (derecha)
    scatter = ax[1].scatter(
        a[:, 0], a[:, 1],
        c=a[:, 2],         # color
        s=a[:, 3],         # tamaño
    )
    ax[1].set_title("Scatter")
    ax[1].set_xlabel("X")
    ax[1].set_ylabel("Y")

    plt.tight_layout()
    plt.show()

def main():
    a = np.array([[1, 2, 10, 1000], [2, 3, 20, 200], [3, 4, 30, 300], [4, 5, 40, 400]])
    subfigures(a)

if __name__ == "__main__":
    main()
