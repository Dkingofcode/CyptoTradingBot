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
import random

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
symbols_df = pd.DataFrame()

###### GETTING ALL THE SYMBOLS ######

for n in markets:
    type = n['info']['type']
    if type == 'Perpetual':
        print(type)
        symbol = n['id']
        print(n['id'])
        temp_df['symbol'] = [symbol]

        # make a df to store
    

        print('--')    

    symbols_df = symbols_df.append(temp_df)

print(symbols_df)  
symbols_df.to_csv('phe_symbols.csv', index=False)  

all_symbols = pd.read_csv('phe_symbols.csv')
print(all_symbols[5:35])

random_symbol_num = random.randrange(0, 78)
random_symbol = all_symbols.iloc[random_symbol_num]['symbol']
print(random_symbol)





# outfile = open('jsontickers.json', 'w')
# json.dump()

# outfile.close()














