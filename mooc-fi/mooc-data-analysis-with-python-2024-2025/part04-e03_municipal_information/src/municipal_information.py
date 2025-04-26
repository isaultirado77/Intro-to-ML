#!/usr/bin/env python3

import pandas as pd
from pathlib import Path


def main():
    filep = Path(__file__).parent / "municipal.tsv"
    df = pd.read_csv(filep, sep='\t')
    shape = df.shape
    columns = df.columns

    print(f"Shape: {shape[0]},{shape[1]}")
    print("Columns:")
    for col in columns:
        print(col)



if __name__ == "__main__":
    main()
