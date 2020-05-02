import requests
import numpy
import time


def BTC_stats():

    response1 = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd/")

    return response1.json()

def ETH_stats():

    response2 = requests.get("https://www.bitstamp.net/api/v2/ticker/ethusd/")

    return response2.json()

def LTC_stats():
    
    response3 = requests.get("https://www.bitstamp.net/api/v2/ticker/ltcusd/")
    
    return response3.json()

def BCH_stats():
    
    response4 = requests.get("https://www.bitstamp.net/api/v2/ticker/bchusd/")
    
    return response4.json()

def XRP_stats():
    
    response5 = requests.get("https://www.bitstamp.net/api/v2/ticker/xrpusd/")
    
    return response5.json()

def sort(final_BTC, final_ETH, final_LTC, final_BCH, final_XRP):
    
    tab = []
    name = []
    
    tab.append(final_BTC)
    tab.append(final_ETH)
    tab.append(final_LTC)
    tab.append(final_BCH)
    tab.append(final_XRP)
    
    name.append("BTC")
    name.append("ETH")
    name.append("LTC")
    name.append("BCH")
    name.append("XRP")
    
    for i in range(4):
        for i in range(4):
            if tab[i]<tab[i+1]:
                
                a=tab[i]
                tab[i]=tab[i+1]
                tab[i+1]=a
                
                b=name[i]
                name[i]=name[i+1]
                name[i+1]=b
    
    return tab, name

    


def timeloop():
    

    while True:
        
        BTC = BTC_stats()
        high_BTC = float(BTC["high"])
        low_BTC = float(BTC["low"])
        final_BTC = ((high_BTC/low_BTC)-1)*100
        
       
        
        ETH = ETH_stats()
        high_ETH = float(ETH["high"])
        low_ETH = float(ETH["low"])
        final_ETH = ((high_ETH/low_ETH)-1)*100
        
        
        
        LTC = LTC_stats()
        high_LTC = float(LTC["high"])
        low_LTC = float(LTC["low"])
        final_LTC = ((high_LTC/low_LTC)-1)*100
        
      
        
        BCH = BCH_stats()
        high_BCH = float(BCH["high"])
        low_BCH = float(BCH["low"])
        final_BCH = ((high_BCH/low_BCH)-1)*100
        
       
        
        XRP = XRP_stats()
        high_XRP = float(XRP["high"])
        low_XRP = float(XRP["low"])
        final_XRP = ((high_XRP/low_XRP)-1)*100
        
        kurs = sort(final_BTC, final_ETH, final_LTC, final_BCH, final_XRP)
        
        
        for i in range(5):
            if kurs[0][i] >= 0:
                print(kurs[1][i],"+",kurs[0][i],"%")
            else:
                print(kurs[1][i],kurs[0][i],"%")
           
        
        print("\n")
        
     


        time.sleep(300)


timeloop() 