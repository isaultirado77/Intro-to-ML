#!/usr/bin/env python3


def main():
    for i in range(1, 11): 
        for j in range(1, 11):
            # Usando :>n para aliear a la izquierda
            print("{:>4}".format(i * j), end="")
        print("")

if __name__ == "__main__":
    main()
