from peregrinearb import create_weighted_multi_exchange_digraph, bellman_ford_multi, \
    print_profit_opportunity_for_path_multi, get_exchanges_for_market
from ccxt import async_support as ccxt
import datetime

# runs with multiple_coins_multiple_exchanges-local

# 'ETH/BTC': ['indodax', 'bitbank', 'mixcoins', 'bitstamp1', 'hitbtc', 'therock', 'coinmate',
#             'hitbtc2', 'dsx', 'crex24', 'exmo', 'yobit', 'gemini', 'bitz', 'zb', 'digifinex',
#             'fcoin', 'fcoinjp', 'adara', 'bleutrade', 'southxchange', 'bitstamp', 'huobipro',
#             'bitbay', 'huobiru', 'coinbasepro', 'luno', 'coinfalcon', 'btcalpha', 'tidex',
#             'lykke', 'latoken', 'bequant', 'coinbaseprime', 'mandala', 'bitlish', 'bitforex',
#             'bitfinex', 'binance', 'binanceus', 'kuna', 'upbit', 'oceanex', 'coss', 'ice3x',
#             'stex', 'rightbtc', 'zaif', 'cex', 'bittrex', 'kraken', 'bitmax', 'lakebtc',
#             'bitso', 'bw', 'bitkk', 'okex', 'gateio', 'okex3', 'coinex', 'poloniex', 'bigone',
#             'livecoin', 'bytetrade', 'buda', 'cobinhood', 'btcmarkets', 'bitmart', 'lbank',
#             'bitflyer', 'anxpro', 'braziliex', 'liquid', 'coinegg', 'kucoin']

collections_dir = '/Volumes/LaCie/programming/jupyter/as-peregrine/peregrinearb/collections/'
wdp_exchanges = get_exchanges_for_market("BTC/USD", collections_dir)
# print(wdp_exchanges)

exchanges = {}
for id in ccxt.exchanges:
    exchange = getattr(ccxt, id)
    # print(id)
    # print(exchange)
    if id is not None:
      exchanges[id] = exchange().name #exchange()['object'].name
      # exchanges[id] = exchange()


suppress_list = ['gdax',
'gatecoin',
'btcx',
'wex',
'getbtc',
'quoinex',
'quadrigacx']

# graph = create_weighted_multi_exchange_digraph(exchanges, log=True, fees=False, suppress = suppress_list)

only_symbols = ['ETH/BTC', 'LTC/BTC']
# remove_pairs = ['B2X/BRL', 'BCH/BRL', 'BTC/BRL', 'BTG/BRL', 'DASH/BRL', 'LTC/BRL']
remove_pairs = ['B2X/BRL']

# graph = create_weighted_multi_exchange_digraph(exchanges, name=True, log=True, fees=True, suppress=None,
#                                                only_symbols=None, remove_pairs=remove_pairs, fee_map=None, symbols_pre_fetch=None)

# 'stex',  can cause rate limiting
# 'binance', can cause rate limiting

exchanges = ['poloniex', 'bitfinex', 'kucoin', 'okex3', 'bittrex', 'coinbasepro']

# exchanges = ['bittrex', 'gemini', 'kraken', 'exmo']

symbols_pre_fetch=['USDK','BTC','TRON','ETH','XTC','QTUM','PLG','ADA','DUSK','PAX','BLOC','BUSD','BCH','USDT']

# single_market_set = {'ETH', 'NEO', 'ADA', 'BTC', 'KAN', 'OKB', 'HBAR', 'BTT', 'TUSD', 'KCS', 'XRP', 'ZIL', 'USD', 'USDK', 'BOLT', 'DAPS', 'UOS', 'USDT', 'ETH', 'TRTL', 'BNB', 'YOU', 'TRX', 'RUB', 'VNT', 'GPS'}

single_market_set = ['BTC', 'USDT', 'ETH', 'XRP', 'LTC', 'EOS', 'BCH', 'PAX', 'TUSD', 'USDC']

# graph = create_weighted_multi_exchange_digraph(exchanges, log=True)

# OK
graph = create_weighted_multi_exchange_digraph(exchanges, log=True, fees=True)
#
# OK
# graph, paths = bellman_ford_multi(graph, 'BTC', loop_from_source=False, unique_paths=True)
# for path in paths:
#     print_profit_opportunity_for_path_multi(graph, path)


# from asquared

while True:
    graph = create_weighted_multi_exchange_digraph(exchanges, log=True, fees=True)
    for mkt in single_market_set:
      graph, paths = bellman_ford_multi(graph, mkt, loop_from_source=False, unique_paths=True)
      for path in paths:
        found = False
        for path in paths:
            found = True
            print(f"{datetime.datetime.now():%D %H:%M:%S.%mm}")
            print('')
            print('--------------------------------------')
            print('')
            print(f'Num steps: {len(path)}')
            print('')
            print_profit_opportunity_for_path_multi(graph, path)
            print('')
            print('--------------------------------------')
            print('')

        if not found:
            print(f'{exchanges} ...')
