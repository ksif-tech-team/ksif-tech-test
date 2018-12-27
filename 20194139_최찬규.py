import numpy as np
import pandas as pd

from pandas import read_csv
df=read_csv("C:/Users/peter/Documents/ksif-tech-test/Price.csv")
df=df.dropna()
df.columns=['date','closed_price']
aapl=df.iloc[::-1]

for i in range(0,len(aapl)-1):
    aapl['draw_down']=(aapl['closed_price'].iloc[i]-aapl['closed_price'].iloc[:i+1].max())/aapl['closed_price'].iloc[i]
aapl['draw_down'].max()