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

params = {'type': 'swap', 'code': 'USD'}

# fetch all the market to get all the symbols
markets = phenex.fetch_markets(params=params)
temp_df = pd.DataFrame()

for n in markets:
    type = n['info']['type']
    if type == 'Perpetual':
        print(type)
        symbol = n['id']
        print(n['id'])
        symbols_df['symbol'] = [symbol]

        # make a df to store
    

        print('--')    

    symbols_df = symbols_df.append(temp_df)

print(symbols_df)    

# outfile = open('jsontickers.json', 'w')
# json.dump()

# outfile.close()














