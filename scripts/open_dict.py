#!/usr/bin/env python3

import pandas as pd

if __name__ == "__main__":
    # An example of loading with pandas with flexible whitesapce
    df = pd.read_csv("dictionaries/chinese.csv", delimiter="\s+")
    print(df)
    breakpoint()
