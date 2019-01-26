# Jiwoo Park Ksif Tech
import pandas as pd
import numpy as np

price = pd.read_csv("./price.csv", index_col=[0], parse_dates=[0], names=["DATE", "PRICE"])
price = price.dropna(0)

def max_draw_down(series):
    # calculate max draw down 
    # find min Idx first if many select latest one
    argmin = np.argmin(series)
    peak = max(series[:argmin + 1])
    trough = min(series)
    return (trough - peak) / peak

print("Sol : {}".format(max_draw_down(price.values)))
