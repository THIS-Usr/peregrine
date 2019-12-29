from peregrinearb import create_weighted_multi_exchange_digraph, bellman_ford_multi, \
    print_profit_opportunity_for_path_multi, get_exchanges_for_market
from ccxt import async_support as ccxt


collections_dir = '/Volumes/LaCie/programming/jupyter/peregrine/wdperegrine/peregrinearb/collections/'



suppress_list = ['gdax',
'gatecoin',
'btcx',
'wex',
'getbtc',
'quoinex',
'quadrigacx']

# graph = create_weighted_multi_exchange_digraph(exchanges, log=True, fees=False, suppress = suppress_list)

suppress = only_symbols = ['B2X/BRL', 'TRY/BTC'] #['ETH/BTC', 'LTC/BTC']
# remove_pairs = ['B2X/BRL', 'BCH/BRL', 'BTC/BRL', 'BTG/BRL', 'DASH/BRL', 'LTC/BRL']
remove_pairs = ['B2X/BRL', 'TRY/BTC']

# 'stex',  can cause rate limiting

# Interesting
# ccxt error
# bibox.py", line 381, in fetch_currencies
# raise AuthenticationError(self.id + " fetchCurrencies is an authenticated endpoint, therefore it requires 'apiKey' and 'secret' credentials.
# If you don't need currency details, set exchange.has['fetchCurrencies'] = False before calling its methods.")

# remove 'bibox',

#  1. remove huobipro
#  2. remove bitmart
#  3. insert hitbtc
#  4. insert fcoin

# 4. hitbtc, kraken -- 119 Thu 19 Dec 2019 09:44:57
# exchanges = ['kraken', 'hitbtc']

# 5. kucoin, okex -- 256 Thu 19 Dec 2019 09:45:30
# exchanges = ['kucoin', 'okex']

# 6. all others
# exchanges = ['kucoin', 'bittrex', 'binance', 'coinbasepro', 'fcoin', 'hitbtc', 'poloniex', 'kraken', 'gemini', 'okex', 'bitstamp', 'bitfinex']

# 7. hitbtc, kraken insert fcoin -- Tue 24 Dec 2019 00:33:36
exchanges = ['kraken', 'hitbtc', 'fcoin']

symbols_pre_fetch=['USDK','BTC','TRON','ETH','XTC','QTUM','PLG','ADA','DUSK','PAX','BLOC','BUSD','BCH','USDT']

single_market_set = {'NEO', 'ADA', 'BTC', 'KAN', 'OKB', 'HBAR', 'BTT', 'TUSD', 'KCS', 'XRP', 'ZIL', 'USD', 'USDK', 'BOLT', 'DAPS', 'UOS', 'USDT', 'ETH', 'TRTL', 'BNB', 'YOU', 'TRX', 'RUB', 'VNT', 'GPS'}


# this version is create_weighted_multi_exchange_digraph(exchanges: list, name=True, log=False, fees=False, suppress=None)

graph = create_weighted_multi_exchange_digraph(exchanges, name=True, log=True, fees=True, suppress=suppress)

# graph = create_weighted_multi_exchange_digraph(exchanges, log=True) # OK Sat 21 Dec 2019 00:08:38

graph, paths = bellman_ford_multi(graph, 'BTC', loop_from_source=False, unique_paths=True)
for path in paths:
    print_profit_opportunity_for_path_multi(graph, path)

# for mkt in single_market_set:
#   graph, paths = bellman_ford_multi(graph, mkt, loop_from_source=False, unique_paths=True)
#   for path in paths:
#     print_profit_opportunity_for_path_multi(graph, path)
#   break

#     below ok
# graph, paths = bellman_ford_multi(graph, 'BTC', loop_from_source=False, unique_paths=True)
# for path in paths:
#     print_profit_opportunity_for_path_multi(graph, path)
