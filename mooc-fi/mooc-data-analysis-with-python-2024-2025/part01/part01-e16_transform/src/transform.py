#!/usr/bin/env python3

def transform(s1: str, s2: str):
    # Convertimos a integer cada s1
    sp1 = list(map(int, s1.split()))
    sp2 = list(map(int, s2.split()))
    return [a * b for a, b in zip(sp1, sp2)]

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
