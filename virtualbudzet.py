import requests
import numpy
import time


def bitbay_ticker():

    response1 = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")

    return response1.json()

def blockchain_ticker():

    response2 = requests.get("https://blockchain.info/ticker")

    return response2.json()

def bitstamp_ticker():
    
    response3 = requests.get("https://www.bitstamp.net/api/ticker")
    
    return response3.json()

def cex_ticker():
    
    response4 = requests.get("https://cex.io/api/ticker/BTC/USD")
    
    return response4.json()


def bestbuy(sale_bitbay, sale_blockchain, sale_bitstamp, sale_cex):
    
    a=float(sale_bitbay)*0.0025
    b=float(sale_blockchain)*0.0027
    c=float(sale_bitstamp)*0.0024
    d=float(sale_cex)*0.0025
    x=float(min(a,b,c,d))
    
    
    if x == a:
        y='bitbay'
        z=float(sale_bitbay)
    elif x == b:
        y='blockchain'
        z=float(sale_blockchain)
    elif x == c:
        y='bitstamp'
        z=float(sale_bitstamp)
    elif x == d:
        y='cex'
        z=float(sale_cex)
        
    
    return x,y,z


def bestsale(buy_bitbay, buy_blockchain, buy_bitstamp, buy_cex):
    
    a=float(buy_bitbay)*0.0025
    b=float(buy_blockchain)*0.0027
    c=float(buy_bitstamp)*0.0024
    d=float(buy_cex)*0.0025
    x=float(max(a,b,c,d))
    
    if x == a:
        y='bitbay'
        z=float(buy_bitbay)
    elif x == b:
        y='blockchain'
        z=float(buy_blockchain)
    elif x == c:
        y='bitstamp'
        z=float(buy_bitstamp)
    elif x == d:
        y='cex'
        z=float(buy_cex)
    
    return x,y,z
 
def arbitration(best_buy,best_sale,Q):
    
    profit = Q*(best_sale[0]-best_buy[0])
    
    return profit

def virtual(money,best_buy):
    ilosc=money/best_buy[2]
    return ilosc

def timeloop():
    budzet=1000

    while True:
        bitbay = bitbay_ticker()
        sale_bitbay = bitbay["ask"]
        buy_bitbay = bitbay["bid"]

        blockchain = blockchain_ticker()
        sale_blockchain = blockchain["USD"]["sell"]
        buy_blockchain = blockchain["USD"]["buy"]

        bitstamp = bitstamp_ticker()
        sale_bitstamp = bitstamp["ask"]
        buy_bitstamp = bitstamp["bid"]

        cex = cex_ticker()
        sale_cex = cex["ask"]
        buy_cex = cex["bid"]  


        best_buy=bestbuy(sale_bitbay, sale_blockchain, sale_bitstamp, sale_cex)
        best_sale=bestsale(buy_bitbay, buy_blockchain, buy_bitstamp, buy_cex)


        Q=virtual(budzet,best_buy)
        zysk = arbitration(best_buy,best_sale,Q)
        budzet=budzet+zysk
        

        print("Na giełdzie",best_buy[1],"można kupić",Q,"BTC za USD po kursie",best_buy[2])
        print("i sprzedać na giełdzie",best_sale[1],"po kursie",best_sale[2],"zyskując",zysk,"USD")
        print("Aktualny budżet",budzet)
        print("\n")
        
        
        time.sleep(5)


timeloop()