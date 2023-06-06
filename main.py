# Import necessary libraries
import pandas as pd
import numpy as np

# Load data
data = pd.read_csv('forex_data.csv')

# Calculate simple moving average
data['SMA'] = data['Close'].rolling(window=20).mean()

# Buy and sell based on SMA
for i in range(1, len(data)):
    if data['SMA'][i] > data['SMA'][i-1]:
        print('Buy')
    elif data['SMA'][i] < data['SMA'][i-1]:
        print('Sell')
    else:
        print('Hold')