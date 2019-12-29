# -*- coding: utf-8 -*-

import asyncio
import os
import sys

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt.async_support as ccxt  # noqa: E402

exchanges_list = ['poloniex', 'bitfinex', 'binance', 'kucoin', 'okex3', 'bittrex', 'stex', 'coinbasepro', 'exmo']
# create exchange objects
exchanges = []

exchanges = [getattr(ccxt, exchange_id)({
        'enableRateLimit': True,  # required by the Manual
    }) for exchange_id in exchanges_list]

async def main():
    # exchange = ccxt.binance({
    #     'enableRateLimit': True,  # required by the Manual
    # })
    for exchange in exchanges:
      for i in range(0, 5):
          # this can be any call instead of fetch_ticker, really
          print(await exchange.fetch_ticker('ETH/BTC'))
      await exchange.close()


asyncio.get_event_loop().run_until_complete(main())
