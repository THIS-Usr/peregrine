# April 2019 triangluation arb test
import asyncio
import time
from peregrinearb import load_exchange_graph, print_profit_opportunity_for_path, bellman_ford

global exchanges

# exchanges = {
#         'bittrex': 0.0025,
#         'binance': 0.00075,
#         'bitfinex2': 0.0025,
#         'bitmex': 0.025,
#         'bithumb': 0.025,
#         'bitstamp': 0.025,
#         'cex': 0.025,
#         'coinbase': 0.0025,
#         # 'cryptopia': 0.0025,
#         'gemini': 0.0025,
#         'hitbtc2': 0.0025,
#         'huobipro': 0.0025,
#         'kraken': 0.0025,
#         'lykke': 0.0,
#         'okex': 0.0025,
#         'poloniex': 0.0025, # .25% taker
#         # 'yobit': 0.0025,
#     }


exchanges = {'exmo':0.002} # .2% taker

# EXMO Tue 24 Dec 2019 17:45:07
# Num steps: 4
#
# Starting with 100 in KICK
# KICK to BTC at 9.979999999999996e-09 = 9.979999999999996e-07
# BTC to USDT at 7268.533800000001 = 0.007253996732399998
# USDT to KICK at 16363.338252172483 = 118.69960221241509

while True:

    for exchange, fees in exchanges.items():
        loop = asyncio.get_event_loop()
        graph = loop.run_until_complete(load_exchange_graph(exchange, fees=fees, depth=True))
        paths = bellman_ford(graph, 'BTC', unique_paths=True, ensure_profit=True)
        found = False
        for path in paths:
            found = True
            print('')
            print('--------------------------------------')
            print('')
            print(exchange.upper())
            print(f'Num steps: {len(path)}')
            print('')
            print_profit_opportunity_for_path(graph, path)
            print('')
            print('--------------------------------------')
            print('')

        if not found:
            print(f'{exchange} ...')
