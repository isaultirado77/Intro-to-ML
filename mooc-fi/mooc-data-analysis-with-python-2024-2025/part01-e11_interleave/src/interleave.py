#!/usr/bin/env python3

def interleave(*lists):
    result = []
    length = min(len(lst) for lst in lists)  # Evita IndexError si las listas son de diferente tamaño
    for i in range(length):
        for lst in lists:
            result.append(lst[i])
    return result

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
