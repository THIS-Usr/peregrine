# # April 2019 triangluation arb test
# OK
from peregrinearb import create_weighted_multi_exchange_digraph, bellman_ford_multi, \
    print_profit_opportunity_for_path_multi


graph = create_weighted_multi_exchange_digraph(['bittrex', 'gemini', 'kraken', 'exmo'], log=True, fees=True)

graph, paths = bellman_ford_multi(graph, 'ETH', loop_from_source=False, unique_paths=True)
for path in paths:
    print_profit_opportunity_for_path_multi(graph, path)