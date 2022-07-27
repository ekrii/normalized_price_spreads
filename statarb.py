import math
import random
import numpy 
import yfinance as yf 
import pandas as pd

msft = yf.Ticker('MSFT')
print(msft)

d = []
for i in msft:
    d.append(i)
    x = pd.array(d)
    print(x)