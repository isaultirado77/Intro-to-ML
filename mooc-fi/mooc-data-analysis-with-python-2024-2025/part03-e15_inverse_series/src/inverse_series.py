#!/usr/bin/env python3

import pandas as pd

def inverse_series(s: pd.Series):
    d = dict()
    idxs = s.index
    values = s.values
    return pd.Series(data=idxs, index=values)

def main():
    d = { 2001 : "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017 : "Trump"}
    s4 = pd.Series(d, name="Presidents")
    inv_s4 = inverse_series(s4)
    print(inv_s4)

if __name__ == "__main__":
    main()
