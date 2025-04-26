#!/usr/bin/env python3

import pandas as pd
import numpy as np


def powers_of_series(series, k):
    data = np.column_stack([series**i for i in range(1, k + 1)])
    df = pd.DataFrame(data, index=series.index)
    df.columns = range(1, k+1)
    return df
    
def main():
    ss = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(ss, 3))
    
if __name__ == "__main__":
    main()
