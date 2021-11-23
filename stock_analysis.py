import pandas as pd # module for reading large amounts of data
#!pip install yfinance  # Google colab doesn't have yfinance installed, let's install this package
import yfinance

stocks = { "AMZN": 100,  # 100 shares of Amazon stock
           "AAPL": 250,  # 250 shares of Apple stock
           "NFLX": 300, # 300 shares of Netflix stock
           "GOOG": 500, # 500 shares of Google stock
           "GME": 100}  # 100 shares of Gamestop stack

total_worth = 0

# the for loop goes through all of the stock
for stock_symbol, number_of_shares in stocks.items():
   stock = yfinance.Ticker (stock_symbol)  # pass in stock_symbol and get stock info
   stock_current_value = stock.info["regularMarketPrice"]  # get current value of stack
   print (stock_symbol + "'s price today is $" + str(stock_current_value))
   # stock value in this portfolio is current value * number of shars
   stock_value = stock_current_value * number_of_shares

   # add this stock_value to total_worth
   total_worth = total_worth + stock_value

# Finished looping through all the stocks, so
# print out total worth
print ("Current portfolio is worth: ")

# round total_worth to 2 decimal places, so see cents.
print ("$" + str (round (total_worth,2)))

