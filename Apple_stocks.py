# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:49:57 2017

@author: vivek
"""

# Suppose we could access yesterday's stock prices as a list, where:

#    The values are the price in dollars of Apple stock.
#    A higher index indicates a later time.
#
#So if the stock cost $500 at 10:30am and $550 at 11:00am, then:
#
#stock_prices_yesterday[60] = 500
#
#Write an efficient function that takes stock_prices_yesterday and returns 
#the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday. 


def get_max_profit(StockList):
    Max=max(StockList)
    Min=min(StockList)
    return Max-Min
stock_prices_yesterday = [10, 7, 5, 8, 11, 9,21,4,21,4,6]    
print(get_max_profit(stock_prices_yesterday))