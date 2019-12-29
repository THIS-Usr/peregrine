import asyncio
from peregrinearb import load_exchange_graph, print_profit_opportunity_for_path, bellman_ford
from datetime import datetime

exchanges = ['poloniex', 'bitfinex', 'binance', 'kucoin', 'okex3', 'bittrex', 'stex']
symbols=['USDK','BTC','TRON','ETH','XTC','QTUM','PLG','ADA','DUSK','PAX','BLOC','BUSD','BCH','USDT']



# graph = create_weighted_multi_exchange_digraph(exchanges, name=False, log=True, fees=True, suppress=None)
#
#
# # graph, 'PLG', loop_from_source=True, ensure_profit=True, unique_paths=True
# graph, paths = bellman_ford_multi(graph, 'BTC', loop_from_source=False, ensure_profit=True, unique_paths=True)
# for path in paths:
#     print_profit_opportunity_for_path_multi(graph, path)
#     print(datetime.now())

loop = asyncio.get_event_loop()
print(datetime.now())
for exchange in exchanges:
  print(exchange)
  graph = loop.run_until_complete(load_exchange_graph(exchange))
  for symbol in symbols:
    paths = bellman_ford(graph, symbol, unique_paths=True)
    for path in paths:
        print(datetime.now())
        print_profit_opportunity_for_path(graph, path)

print(datetime.now())
