#/Volumes/LaCie/programming/jupyter/wd-rgg81peregrine/rgg81/peregrinearb/collections
file_path = '/Volumes/LaCie/programming/jupyter/peregrine/wdperegrine/peregrinearb/collections/'

#Multiples Exchange/ One Currency
# XVG/DOGE BTC/USD
from peregrinearb import get_opportunity_for_market, async_get_exchanges_for_market, load_exchange_graph# changed from async_get_exchanges_for_market AS
import asyncio
from datetime import datetime

import ccxt.async_support as ccxt  # noqa: E402

collections_dir = file_path #'/Users/wardbradt/cs/peregrine/'

symbols=['USDK','BTC','TRON','ETH','XTC','QTUM','PLG','ADA','DUSK','PAX','BLOC','BUSD','BCH','USDT']

# symbols=['USDK/PLG','BTC/ETH','BTC/XTC','USDT/BLOC']
# 'ETH/BTC', 'BTC/USDT', 'NEO/ETH',
# following pairs not found as ccxt exchange traded markets
symbols_set = ['DAPS/USDT',
'USDT/BOLT',
'ETH/ZIL',
'TUSD/XRP',
'RUB/ETH',
'VNT/USDK',
'OKB/NEO',
'BTC/GPS',
'XRP/TUSD',
'USDT/DAPS',
'USDT/VNT',
'HBAR/BTC',
'ETH/KCS',
'KAN/USD',
'TRTL/ETH',
'GPS/ETH',
'BTC/ADA',
'BTC/TRTL',
'ZIL/BNB',
'BNB/RUB',
'YOU/USDT',
'USDT/KAN',
'USD/HBAR',
'ETH/YOU',
'ADA/USD',
'BOLT/BTC',
'UOS/BTC',
'BTT/TRX',
'USD/UOS',
'USDK/OKB',
'TRX/BTT',
'KCS/USDT']

import json
# print(ccxt.exchanges)

# exchanges = [getattr(ccxt, exchange_id)({
#         'enableRateLimit': True,  # required by the Manual
#     }) for exchange_id in ccxt.exchanges]
#
# print(exchanges)
with open('{}ccxt_all_markets_(1405).json'.format(collections_dir)) as f:
  symbols_set = json.load(f)


def compare_collections(collections_dir):
  try:
    with open('{}collections.01.json'.format(collections_dir)) as f:
      collections = json.load(f)
    for market_name, exchanges in collections.items():
      # print(market_name)
      print(exchanges)
      # for symbol in symbols_set:
      #   if market_name == symbol:
      #     print(market_name)
      #     print(exchanges)
  except FileNotFoundError:
    print('error')

compare_collections(collections_dir)

async def main():

  # print(get_opportunity_for_market('BTC/ADA', collections_dir))
  print(datetime.now())


# asyncio.get_event_loop().run_until_complete(main())
# opportunity = asyncio.get_event_loop().run_until_complete(get_opportunity_for_market('BTC/ADA', collections_dir))
# print(opportunity)
# asyncio.run(main(opportunity))


btc_exchanges = ['indodax', 'bitbank', 'mixcoins', 'bitstamp1', 'hitbtc', 'therock', 'coinmate',
            'hitbtc2', 'dsx', 'crex24', 'exmo', 'yobit', 'gemini', 'bitz', 'zb', 'digifinex',
            'fcoin', 'fcoinjp', 'adara', 'bleutrade', 'southxchange', 'bitstamp', 'huobipro',
            'bitbay', 'huobiru', 'coinbasepro', 'luno', 'coinfalcon', 'btcalpha', 'tidex',
            'lykke', 'latoken', 'bequant', 'coinbaseprime', 'mandala', 'bitlish', 'bitforex',
            'bitfinex', 'binance', 'binanceus', 'kuna', 'upbit', 'oceanex', 'coss', 'ice3x',
            'stex', 'rightbtc', 'zaif', 'cex', 'bittrex', 'kraken', 'bitmax', 'lakebtc',
            'bitso', 'bw', 'bitkk', 'okex', 'gateio', 'okex3', 'coinex', 'poloniex', 'bigone',
            'livecoin', 'bytetrade', 'buda', 'cobinhood', 'btcmarkets', 'bitmart', 'lbank',
            'bitflyer', 'anxpro', 'braziliex', 'liquid', 'coinegg', 'kucoin']

# loop = asyncio.get_event_loop()
#
# print(btc_exchanges[0])
#
# async def load(btc_exchanges):
#   return await load_exchange_graph(btc_exchanges[0])
#
#
# graph = loop.run_until_complete(load(btc_exchanges))
# print(graph)

