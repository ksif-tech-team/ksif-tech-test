import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def calculateMdd(df, var, winodw = 20):
    '''

    Window refers how window to look back in calculating maximum drawdown.

    :param winodw:
    :return:
    '''
    return df.prc.rolling(window = window).apply(lambda x : (min(x)-max(x))/max(x))

#preproc

df = pd.read_csv("Price.csv")
df.dropna(inplace=True)
#df.iloc[:,0] = df.iloc[:,0].apply(lambda x: pd.Timestamp(x))
df.iloc[:,0] = pd.to_datetime(df.iloc[:,0])
df.columns = ['date', 'prc']
df.sort_values(['date'],inplace=True)
#df['ret'] = df.prc.pct_change(1)
df.set_index('date',inplace=True)

window = 10

df['mdd_noFunc'] = df.prc.rolling(window = window).apply(lambda x : (min(x)-max(x))/max(x))

df['mdd1'] = calculateMdd(df,'ret',window)

df.mdd1.plot()
plt.show()