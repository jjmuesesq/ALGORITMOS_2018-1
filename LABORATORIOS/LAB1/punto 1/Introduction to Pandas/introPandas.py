# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 17:19:01 2018

@author: Jhon Jairo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

returns = pd.DataFrame(np.random.normal(1.0, 0.03, (100, 10)))
prices = returns.cumprod()
prices.plot()
plt.title('Randomly-generated Prices')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend(loc=0);

#PANDAS DATASTRUCTURE
#Series
s = pd.Series([1, 2, np.nan, 4, 5])
print (s)
print (s.name)

s.name = "Toy Series"
print (s.name)
print (s.index)
new_index = pd.date_range("2016-01-01", periods=len(s), freq="D")
print (new_index)

s.index = new_index
print (s.index)

print ("First element of the series: ", s.iloc[0])
print ("Last element of the series: ", s.iloc[len(s)-1])

print(s.iloc[:2])

start = 0
end = len(s) - 1
step = 1

print(s.iloc[start:end:step])

print(s.iloc[::-1])
print(s.iloc[-2:-4:-1])
print(s.loc['2016-01-01'])
print(s.loc['2016-01-02':'2016-01-04'])

#Boolean Indexing
print(s<3)
print (s.loc[s < 3])
print (s.loc[(s < 3) & (s > 1)])

symbol = "CMG"
start = "2012-01-01"
end = "2016-01-01"
prices = get_pricing(symbol, start_date=start, end_date=end, fields="price")
