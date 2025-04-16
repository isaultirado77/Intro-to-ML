#!/usr/bin/env python3

def merge(L1, L2):
    merged = []
    i = j = 0
    
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1
    
    while i < len(L1):
        merged.append(L1[i])
        i += 1
    
    while j < len(L2):
        merged.append(L2[j])
        j += 1
    
    return merged

def main():
    print(merge([1,5,9,12], [2,6,10]))
    pass

if __name__ == "__main__":
    main()
