#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    sqrt_discriminant = math.sqrt(discriminant)
    solution1 = (-b + sqrt_discriminant) / (2*a)
    solution2 = (-b - sqrt_discriminant) / (2*a)
    return (solution1, solution2)


def main():
    print(solve_quadratic(3, 9, 6))
    #print(solve_quadratic(1, -3, 2))
    #print(solve_quadratic(1, 2, 1))

if __name__ == "__main__":
    main()
