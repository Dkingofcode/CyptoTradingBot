'''
this bot trades over 58+ different cryptos
it looks for opportunties in each market, 
makes decisions executes orders automatically

'''




import ccxt
import json
import pandas as pd
import numpy as np
import dontshare_config as ds
from dateline import date, datetime, timezone, tzinfo
import time, schedule
import nice_funcs as n


phenex = ccxt.phenex({
    'enableRateLimit': True,
    'apiKey': ds.xP_KEY,
    'secret': ds.xP_SECRET
})

symbol = 'uBTCUSD'
pos_size = 1
target = 9 # percentage gain i want
max_loss = -8

params = {'timeInForce': 'PostOnly', }

# fetch all the market to get all the symbols
print(phenex.fetch_markets())


















