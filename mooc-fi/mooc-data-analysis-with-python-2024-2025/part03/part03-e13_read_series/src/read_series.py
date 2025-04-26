#!/usr/bin/env python3

import pandas as pd

def read_series():
    x = list()
    while True: 
        value = input()
        if value == "":
            break
        x.append(value)

    return pd.Series(data=x)

def series_info(s: pd.Series): 
    print(f"Name: {s.name},\ndtype: {s.dtype},\nsize: {s.size}")
    print(f"index: {s.index}")
    print(f"values: {s.values}")

def main():
    s = read_series()
    series_info(s)

if __name__ == "__main__":
    main()
