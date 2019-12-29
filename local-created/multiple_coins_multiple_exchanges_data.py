from __future__ import print_function

from peregrinearb import create_weighted_multi_exchange_digraph, bellman_ford_multi, \
    print_profit_opportunity_for_path_multi

import pymysql

import urllib.request
import numpy as np
import mysql.connector as mysql

from datetime import date, datetime, timedelta


# mysqlclient (a maintained fork of MySQL-Python)
# engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')

# PyMySQL
# engine = create_engine('mysql+pymysql://scott:tiger@localhost/foo')


import sqlalchemy as sql
import pandas as pd



connect_string = 'mysql+pymysql://root:mentrandr@localhost/asperegrine' # OK

sql_engine = sql.create_engine(connect_string)



# 'tradeogre' not supported
# 'citex' not supported
# 'stex' gives absurd results here - need to investigate esp. as multiple coins one exchange
# 'stex' also doesn't like multiple requests

exchanges = ['poloniex', 'bitfinex', 'binance', 'kucoin', 'okex3', 'bittrex']
symbols_pre_fetch=['USDK','BTC','TRON','ETH','XTC','QTUM','PLG','ADA','DUSK','PAX','BLOC','BUSD','BCH','USDT']
# graph = create_weighted_multi_exchange_digraph(exchanges, name=True, log=True, fees=True, suppress=None,
#                                                only_symbols=symbols_pre_fetch, remove_pairs=None, fee_map=None, symbols_pre_fetch=symbols_pre_fetch)

# OK with previous version of multi-exchange
#  --->
# Starting with 100 in BTC
# BTC to PLG at 12468749.999999981 = 1246874999.999998 on bittrex for PLG/BTC
# PLG to USDT at 0.00414585 = 5169356.718749993 on okex3 for PLG/USDT
# USDT to BLOC at 1998.3996799359873 = 10330440812.22493 on kucoin for BLOC/USDT
# BLOC to BTC at 2.5973999999999986e-07 = 2683.228696567302 on okex3 for BLOC/BTC
graph = create_weighted_multi_exchange_digraph(exchanges, name=True, log=True, fees=True, suppress=None)


now = datetime.now()

print(now)

# cursor.execute("INSERT INTO table (name, id, datecolumn) VALUES (%s, %s, '%s')",
#                ("name", 4, now))

graph, paths = bellman_ford_multi(graph, 'PLG', loop_from_source=False, unique_paths=True)
for path in paths:
    result, is_profitable = print_profit_opportunity_for_path_multi(graph, path, False)
    print(result)
    print(is_profitable)



# query = "select * from `multicoin-exchange`"
# df = pd.read_sql_query(query, sql_engine)
#
# print(df)
