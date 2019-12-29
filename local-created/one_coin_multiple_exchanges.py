#/Volumes/LaCie/programming/jupyter/wd-rgg81peregrine/rgg81/peregrinearb/collections
file_path = '/Volumes/LaCie/programming/jupyter/peregrine/wdperegrine/peregrinearb/collections/'

#Multiples Exchange/ One Currency
# XVG/DOGE BTC/USD
from peregrinearb import get_opportunity_for_market, async_get_exchanges_for_market, load_exchange_graph# changed from async_get_exchanges_for_market AS
import asyncio

collections_dir = file_path #'/Users/wardbradt/cs/peregrine/'
opportunity = asyncio.get_event_loop().run_until_complete(get_opportunity_for_market("ETH/BTC", collections_dir))
# opportunity = asyncio.get_event_loop().run_until_complete(get_opportunity_for_market("XVG/DOGE", exchanges[id]))
# opportunity = get_opportunity_for_market("XVG/DOGE", exchanges[id])
print(opportunity)

# exchanges = asyncio.get_event_loop().run_until_complete(async_get_exchanges_for_market("BTC/USD", collections_dir))#("BTC/USD", collections_dir))
#
# '''following works errors in wdperegrine and rgg81 (peregrine) when collections.json found with first char of path
# string not found
# '''
# opportunity = asyncio.get_event_loop().run_until_complete(get_opportunity_for_market("BTC/USD", collections_dir))
# print(opportunity)
#
# '''following works with errors in wdperegrine and rgg81 (peregrine) when collections.json not found:-
# AttributeError: module 'ccxt.async_support' has no attribute '/'
# '''
# # for collection in exchanges:
# #     opportunity = asyncio.get_event_loop().run_until_complete(get_opportunity_for_market(collection,exchanges[collection], name=True))
# #     print(opportunity)

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

