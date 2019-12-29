from peregrinearb import create_weighted_multi_exchange_digraph, bellman_ford_multi, print_profit_opportunity_for_path_multi

# 'exmo',  time out at moment, and we don't deal with the error -- bad
graph = create_weighted_multi_exchange_digraph(['bittrex', 'gemini'], log=True)
path = bellman_ford_multi(graph, 'ETH')
print_profit_opportunity_for_path_multi(graph, path)
