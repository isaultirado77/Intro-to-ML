#!/usr/bin/env python3

def main():
    s = [f"({i}, {j})" for i in range(1, 7) for j in range(1, 7) if i + j == 5]
    for i in range(len(s)): 
        print(s[i])

if __name__ == "__main__":
    main()
