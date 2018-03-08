import urllib2
import json
import time



def function():
    url = 'https://api.gdax.com/products/BTC-EUR/ticker'
    url2 = 'https://api.gdax.com/products/BTC-GBP/ticker'
    url3 = 'http://www.apilayer.net/api/live?access_key=168c30b73840aa38cb8139c921e128b7&source=USD&currencies=GBP,EUR'

    json_obj = urllib2.urlopen(url)
    json_obj2 = urllib2.urlopen(url2)
    json_obj3 = urllib2.urlopen(url3)

    data = json.load(json_obj)
    data2 = json.load(json_obj2)
    data3 = json.load(json_obj3)
    BE =  float(data['price'])
    BG = float(data2['price'])

    print BE/BG

    GBP = data3['quotes']['USDGBP']
    EUR = data3['quotes']['USDEUR']

    print EUR/GBP

    if (EUR/GBP) > (BE/BG):
        print "BUY BTC on GBP / SELL BTC on EUR"

    if (EUR/GBP) < (BE/BG):
        print "BUY BTC on EUR / SELL BTC on GBP"
    time.sleep(10)
    function()

function()
