import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
# this returns a dict of nested lists
# becuase we only want the price
bitcoin_price_data = bitcoin_data['prices']

import pandas as pd
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')
# we are appending the new column 'Date' to the df
candlestick_data = data.groupby(data.Date.dt.date).agg({'Price' : ['min', 'max', 'first', 'last']})

#using PLOTLY which I might have to install
fig = go.Figure(data=[go.Candlestick(x= candlestick_data.index, open=candlestick_data['Price']['first'], high=candlestick_data['Price']['max'], low=candlestick_data['Price']['min'], close=candlestick_data['Price']['last'])])

fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Date' , yaxis_title='Price (USD $)', title='Bitcoin Candlestick Chart Over Past 30 Days')

plot(fig, filename='bitcoin_candlestick_graph.html')

#on the Watson studio platform we use for the labs, they say we need to click on the
# html file, click trust and then we will be able to see it
