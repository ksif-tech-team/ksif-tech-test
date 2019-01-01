
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

os.chdir(r'C:\Users\82103\Desktop\ksif-tech-test-master')

df = pd.read_csv('Price.csv',header=None)

#reverse order
df = df.iloc[::-1]

df.columns = ['Date','AAPL_P']

df = df.set_index('Date')
df = df.dropna()
df.index = pd.to_datetime(df.index)


# In[2]:


#mdd
max = df['AAPL_P'][0]
min = df['AAPL_P'][0]

# from / trough / to / depth / length / to trough / recovery
# depth in percentage terms not in absolute value

min = 0
mdd = []
down = 0
for i in range(len(df['AAPL_P'])):
    
    if down == 1 and df['AAPL_P'][i] >= max:
        # depth in absolute value: max - min
        mdd.append([df.index[start],df.index[lowest],df.index[i],1 - min/max,i-start,lowest-start,i-lowest])
        down = 0

    if df['AAPL_P'][i] >= max:
        start = i
        max = df['AAPL_P'][i]
        min = df['AAPL_P'][i]
    
    if df['AAPL_P'][i] < max:
        if df['AAPL_P'][i] <= min:
            min = df['AAPL_P'][i]
            lowest = i
            down = 1
            
if start < lowest:
    print("The latest highest/lowest points are",max,"/",min,".")
    print("The date of lowest point being",df.index[lowest].strftime('%Y-%m-%d'))
    print("This stock has not recovered for",i-start,"days since",df.index[start].strftime('%Y-%m-%d'))
    print("This stock has recovered by",round((df['AAPL_P'][i]-min)/(max-min)*100,2),'%')


# In[3]:


# sort so that highest mdd comes first

for step in range(len(mdd),1,-1):
    for i in range(1,step):
        if (mdd[i][3] > mdd[i-1][3]):
            mdd[i], mdd[i-1] = mdd[i-1], mdd[i]


# In[4]:


data = pd.DataFrame(mdd)

data.columns= ['From','Trough','To','Depth','Length','To Trough','Recovery']
data


# In[5]:


fig, ax = plt.subplots()
ax.plot(df['AAPL_P'])

# draw red lines to better visulaize the mdds

for i in range(len(mdd)):
    ax.hlines(y=df['AAPL_P'][mdd[i][0]], xmin=mdd[i][0], xmax=mdd[i][2], linewidth=2, color='r')

plt.show()

