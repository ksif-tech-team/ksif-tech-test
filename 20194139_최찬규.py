import numpy as np
import pandas as pd

## 파일 불러오기
from pandas import read_csv
df=read_csv("C:/Users/peter/Documents/ksif-tech-test/Price.csv")

## NaN 값 없애기
df=df.dropna()

## 칼럼 이름 넣기
df.columns=['date','closed_price']

## 역순으로 배열하기
aapl=df.iloc[::-1]

## draw down 칼럼을 만들어 계산하기
for i in range(0,len(aapl)-1):
    aapl['draw_down']=(aapl['closed_price'].iloc[i]-aapl['closed_price'].iloc[:i+1].max())/aapl['closed_price'].iloc[i]

## draw down 중 최댓값 찾기
aapl['draw_down'].max()