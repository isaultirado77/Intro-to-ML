#!/usr/bin/env python3

import pandas as pd

def create_series(L1: list, L2: list):
    ids = ['a', 'b', 'c']
    return (pd.Series(data=L1, index=ids), pd.Series(data=L2, index=ids))
    
def modify_series(s1: pd.Series, s2: pd.Series):
    s1['d'] = s2.loc['b']
    s2 = s2.drop('b')
    return (s1, s2)
    
def main():
    l1 = (1, 2, 3)
    l2 = (4, 5, 6)
    s1, s2 = create_series(l1, l2)
    ss1, ss2 = modify_series(s1, s2)
    print(ss1)
    print(ss2)
    s1.__add__(s2)
    
if __name__ == "__main__":
    main()
