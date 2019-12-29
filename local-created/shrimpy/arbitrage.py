# import the Shrimpy library for crypto exchange websockets
import shrimpy
import os

public_key = os.environ.get("SHRIMPY_PUBLIC_KEY")
private_key = os.environ.get("SHRIMPY_SECRET_KEY")

print(public_key)

# a sample error handler, it simply prints the incoming error
def error_handler(err):
    print(err)

exchanges_bbo = {}

# define the handler to manage the output stream
def handler(msg):
    bid_price = msg['content']['bids'][0]['price']
    ask_price = msg['content']['asks'][0]['price']
    exchanges_bbo[msg['exchange']] = {'bid': float(bid_price), 'ask': float(ask_price)}
    best_bid = 0.0
    best_ask = 100000.0
    best_bid_exchange = ''
    best_ask_exchange = ''
    for key, value in exchanges_bbo.items():
        if value['bid'] > best_bid:
            best_bid = value['bid']
            best_bid_exchange = key
        if value['ask'] < best_ask:
            best_ask = value['ask']
            best_ask_exchange = key
    if best_bid > best_ask:
        print("sell on " + best_bid_exchange + " for " + str(best_bid))
        print("buy on " + best_ask_exchange + " for " + str(best_ask))
    else:
        print("No Arbitrage Available")


# input your Shrimpy public and private key
# public_key = 'd085a9e31c3b43c71cefda96b5322b52755243c36fc3ac6e571cb640e7e17440'
# private_key = 'afbf3b04050cc8cc8748af60882051076b9d032355c7eb3e600879368ca541609baefc1aaebd79723de76dbaea9e1e58acbe92d4cb96126cb77f25da74e66b70'

# create the Shrimpy websocket client
api_client = shrimpy.ShrimpyApiClient(public_key, private_key)
raw_token = api_client.get_token()
if raw_token is not None:
  print(raw_token)
client = shrimpy.ShrimpyWsClient(error_handler, raw_token['token'])


# connect to the Shrimpy websocket and subscribe
client.connect()

# select exchanges to arbitrage
exchanges = ["bittrex", "binance", "kucoin", "okex"]
# pair = "btc-usdt"
pair = "bloc-usdt"

# restrict
x = 0
while x < 10:
  # subscribe to the websockets for the given pair on each exchange
  for exchange in exchanges:
      subscribe_data = {
          "type": "subscribe",
          "exchange": exchange,
          "pair": pair,
          "channel": "bbo"
      }
      client.subscribe(subscribe_data, handler)
  x +=1
client.disconnect()
