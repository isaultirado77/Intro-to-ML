#!/usr/bin/env python3

def detect_ranges(lst):
    if not lst:
        return []
    
    lst = sorted(lst)
    result = []
    start = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1] + 1:
            continue
        else:
            if start == lst[i-1]:
                result.append(start)
            else:
                result.append((start, lst[i-1] + 1))
            start = lst[i]
    
    # Handle the last element(s)
    if start == lst[-1]:
        result.append(start)
    else:
        result.append((start, lst[-1] + 1))
    
    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
