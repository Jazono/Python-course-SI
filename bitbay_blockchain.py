import requests


def bitbay_orderbook():

    response = requests.get("https://bitbay.net/API/Public/BTCUSD/orderbook.json")

    return response.json()


def orderbook():
    
    order_BTC_USD = bitbay_orderbook()
    sale = order_BTC_USD['asks']
    buy = order_BTC_USD['bids']
    a=0
    b=0
    
    print("SALE")
    for i in range (10):
        print(sale[a])
        a=a+1
    
    print("BUY")
    for i in range (10):
        print(buy[b])
        b=b+1

def bitbay_ticker():

    response = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")

    return response.json()

def blockchain_ticker():

    response = requests.get("https://blockchain.info/ticker")

    return response.json()

def comparison():
    
    bitbay = bitbay_ticker()
    sale_bitbay = bitbay["ask"]
    buy_bitbay = bitbay["bid"]
    
    blockchain = blockchain_ticker()
    sale_blockchain = blockchain["USD"]["sell"]
    buy_blockchain = blockchain["USD"]["buy"]
    
    if sale_bitbay < sale_blockchain:
        print(" ")
        print("Buy on bitbay.net")
    else:
        print(" ")
        print("Buy on blockchain.info")
    
    
    if buy_bitbay > buy_blockchain:
        print(" ")
        print("Sale on bitbay.net")
    else:
        print(" ")
        print("Sale on blockchain.info")
    

orderbook()
comparison()