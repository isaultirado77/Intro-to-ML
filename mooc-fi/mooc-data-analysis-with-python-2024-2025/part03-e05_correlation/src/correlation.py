#!/usr/bin/env python3

import scipy.stats as stats
import numpy as np
from pathlib import Path


def load():
    import pandas as pd
    base_path = Path(__file__).parent
    file_path = base_path / "iris.csv"
    return pd.read_csv(file_path).drop('species', axis=1).values

def lengths():
    data = load()
    pearson_result = stats.pearsonr(data[:, 0], data[:, 2])
    return pearson_result[0]

def correlations():
    data = load()
    return np.corrcoef(data.T)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
