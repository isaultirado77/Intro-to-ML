#!/usr/bin/env python3

def find_matching(L, pattern):
    idx = []
    for i, s in enumerate(L):
        if pattern in s: 
            idx.append(i)
    return idx

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
