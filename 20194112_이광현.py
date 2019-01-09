# coding: utf-8
import pandas as pd

# MDD 구하는 함수
def getMdd(frame):
    high = frame['Price'][0]
    mdd = 0;

    for i in frame['Price']:
        dd = (i/high)-1
        if dd<mdd : 
            mdd = dd
        if i>high :
            high = i

    return mdd

# Data pretreatment
df = (pd.read_csv('Price.csv', encoding='UTF-8')).dropna(axis=0)
df.columns = ['Date', 'Price']
df['Date'] = pd.to_datetime(df.Date)
df = df.sort_values(by = 'Date')

# getMdd
print(getMdd(df))






