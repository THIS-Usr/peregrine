# This code is modified from examples/test_build_collections.py
from peregrinearb.async_build_markets import build_specific_collections, build_collections
from peregrinearb import create_weighted_multi_exchange_digraph, bellman_ford_multi, \
    print_profit_opportunity_for_path_multi

from datetime import datetime
print('time')
print(datetime.now())


# This is a dict of the collections only containing exchanges which have the fetch_order_book, create_market_buy_order,
# create_market_sell_order, create_limit_buy_order, and create_limit_sell_order functions.
# It would be interesting to get this to work!
# specific_collections = build_specific_collections(has={'fetchOrderBook': True, 'createOrder': True})
#
# if specific_collections is None:
#   specific_collections = build_collections()
#
# print(specific_collections)

exchanges = ['poloniex', 'bitfinex', 'binance', 'kucoin', 'okex3', 'bittrex']
symbols_pre_fetch=['USDK','BTC','TRON','ETH','XTC','QTUM','PLG','ADA','DUSK','PAX','BLOC','BUSD','BCH','USDT']



graph = create_weighted_multi_exchange_digraph(exchanges, name=False, log=True, fees=True, suppress=None)


# graph, 'PLG', loop_from_source=True, ensure_profit=True, unique_paths=True
graph, paths = bellman_ford_multi(graph, 'BTC', loop_from_source=False, ensure_profit=True, unique_paths=True)
for path in paths:
    print_profit_opportunity_for_path_multi(graph, path)
    print(datetime.now())
