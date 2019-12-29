import ccxt.async_support as ccxt
import asyncio

exchanges = {}  # a placeholder for your instances

for id in ccxt.exchanges:
    exchange = getattr(ccxt, id)
    exchanges[id] = exchange()

# After running the code you provided, when I run ...
order_book = asyncio.get_event_loop().run_until_complete(exchanges['bittrex'].fetch_order_book('ETH/BTC'))
print(order_book)
