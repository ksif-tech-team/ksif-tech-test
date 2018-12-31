#파일 불러오기
from pandas import read_csv
aapl=read_csv("C:/Users/peter/Documents/ksif-tech-test/Price.csv")

#일별 수익률 계산하기
aapl=aapl.dropna()
aapl.columns=['date','closed_price']
aapl['returns']=(aapl['closed_price']-aapl['closed_price'].shift(-1))/aapl['closed_price'].shift(-1)

#누적 수익률 구하기
cum_r=aapl['returns'].iloc[::-1].add(1).cumprod()
dd=cum_r.div(cum_r.cummax()).sub(1)

#누적수익률 중 최솟값 찾기
mdd=dd.min()