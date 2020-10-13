import tensorflow as tf

import numpy as np
import pandas as pd
import os
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.pipeline import make_pipeline
from scipy import signal
import pickle
import robin_stocks as r
import pyotp

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

robinhood_user = os.environ.get('robinhood_user')
robinhood_pass = os.environ.get('robinhood_pass')
robinhood_multi = os.environ.get('robinhood_multi')

basket = ['XRX', 'NLOK', 'STX', 'AMD', 'IT', 'CSCO', 'INTC', 'MSFT', 'IBM']
# 'NVDA', 'AAPL'

totp = pyotp.TOTP(str(robinhood_multi)).now()
login = r.login(robinhood_user, robinhood_pass, mfa_code=totp)

# Current stock portfolio
my_stocks = r.build_holdings()
for key, value in my_stocks.items():
    print(key, value)

df = pd.DataFrame(my_stocks)
df = df.T
df['ticker'] = df.index
df = df.reset_index(drop=True)

# Get historical data of stocks in basket
stock_data = r.stocks.get_stock_historicals(basket, interval='day', span='3month', bounds='regular')
stock_df = pd.DataFrame(stock_data)

# Switching to floats so plot can read the numbers
column_list = ['close_price', 'high_price', 'low_price', 'open_price']
for i in column_list:
    stock_df[i] = stock_df[i].astype(float)

# Line plot each stock ticker with random color
for i in basket:
    plt.plot('begins_at', 'close_price', data=stock_df[stock_df['symbol'] == i], color=np.random.rand(3,), label=i)
plt.legend()

