#!/usr/bin/env python3

from collections import defaultdict

def reverse_dictionary(d):
    new_d = defaultdict(list)
    for key, values in d.items():
        for val in values: 
            new_d[val].append(key)
    return dict(new_d)

def main():
    dtest = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(dtest))

if __name__ == "__main__":
    main()
