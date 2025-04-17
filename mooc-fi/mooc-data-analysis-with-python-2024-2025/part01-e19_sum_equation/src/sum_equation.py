#!/usr/bin/env python3

def sum_equation(L: list):
    if len(L) == 0: 
        return "0 = 0"
    return " + ".join(map(str, L)) + f" = {sum(L)}"

def main():
    print(sum_equation([1, 2, 3]))

if __name__ == "__main__":
    main()
