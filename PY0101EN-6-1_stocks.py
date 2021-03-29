import yfinance as yf
import pandas as pd

# Using the Ticker module we can create an object that will allow us to access functions to extract data.
apple = yf.Ticker("AAPL")
'''
Now we can access functions and variables to extract the type of data we need.
You can view them and what they represent here https://aroussi.com/post/python-yahoo-finance.
'''
apple_info=apple.info #extracts a python dict
#print(apple_info)

'''
Using the history() method we can get the share price of the stock over a certain period of time.
Using the period parameter we can set how far back from the present to get data.
The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo,
1 year (1y), 2y, 5y, 10y, ytd, and max.
'''
apple_share_price_data = apple.history(period="max")
'''
The format that the data is returned in is a Pandas DataFrame.
With the Date as the index the share Open, High, Low, Close, Volume,
and Stock Splits are given for each day.
'''
print(apple_share_price_data.head())
'''
We can reset the index of the DataFrame with the reset_index function.
We also set the inplace paramter to True so the change takes place to the DataFrame itself.
'''
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open")

'''
 ----- EXTRACTING DIVIDENDS -----
Using the variable dividends we can get a dataframe of the data.
The period of the data is given by the period defined in the 'history` function.
'''

apple.dividends
apple.dividends.plot()
'''
United States
Technology
325058400'''
