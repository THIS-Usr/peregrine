from peregrinearb import create_weighted_multi_exchange_digraph, bellman_ford_multi, print_profit_opportunity_for_path_multi

# test 1 -- error   File "/Volumes/LaCie/programming/jupyter/peregrine/networkx/networkx/classes/coreviews.py", line 103, in __getitem__
#     return AdjacencyView(self._atlas[name])
# KeyError: <networkx.classes.digraph.DiGraph object at 0x106b16890>

# 'exmo',  time out at moment, and we don't deal with the error -- bad
# below does not work - why?
# graph = create_weighted_multi_exchange_digraph(['bittrex', 'gemini'], log=True)
# path = bellman_ford_multi(graph, 'ETH')
# print_profit_opportunity_for_path_multi(graph, path)

# 1. what is the need for 'single_market_set'?
# 2. can I add to or subtract from it?

# exchanges = ['bittrex', 'gemini'] # -- no
exchanges = ['bittrex', 'gemini', 'kraken', 'exmo']
single_market_set = {'NEO', 'ADA', 'BTC', 'KAN', 'OKB', 'HBAR', 'BTT', 'TUSD', 'KCS', 'XRP', 'ZIL', 'USD', 'USDK', 'BOLT', 'DAPS', 'UOS', 'USDT', 'ETH', 'TRTL', 'BNB', 'YOU', 'TRX', 'RUB', 'VNT', 'GPS'}

graph = create_weighted_multi_exchange_digraph(exchanges, log=True, fees=True)
# for mkt in single_market_set:
#   graph, paths = bellman_ford_multi(graph, mkt, loop_from_source=False, unique_paths=True)
#   for path in paths:
#     found = False
#     for path in paths:
#       found = True
#       print('')
#       print('--------------------------------------')
#       print('')
#       print(f'Num steps: {len(path)}')
#       print('')
#       print_profit_opportunity_for_path_multi(graph, path)
#       print('')
#       print('--------------------------------------')
#       print('')
#
#     if not found:
#       print(f'{exchanges} ...')

graph, paths = bellman_ford_multi(graph, 'ETH', loop_from_source=False, unique_paths=True)
for path in paths:
  found = False
  for path in paths:
    found = True
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
