#!/usr/bin/env python3

import pandas as pd

def cities():
    cols = ['Population', 'Total area']
    idx = ['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu']
    dat = [[643272, 715.48], [279044, 528.03], [231853, 689.59], [223027, 240.35], [201810, 3817.52]]
    return pd.DataFrame(data=dat, columns=cols, index=idx)
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
