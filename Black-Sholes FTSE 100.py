import time
import pandas as pd
import numpy
import statistics
from scipy.stats import norm


print('loading data...')
data = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=^FTSE&outputsize=full&apikey=QF2HHIIEPV3QYGO8&datatype=csv')
print data
close = data.close.tolist()
numpy.trim_zeros(close)
aclose = [x for x in close if x>100]
try:
    aclose.remove(0.0)
    aclose.remove(0)
    aclose.remove('0.0')
except ValueError:
    print "no zeros found"

#print aclose
ret = []

for i in range(len(aclose)-1):
    a = (aclose[i]-aclose[i+1])
    b = aclose[i+1]
    float(a)
    float(b)
    c = 100 * a/b
    print c
    ret.append(c)
#print ret    
    
si = statistics.stdev(ret)
sig = (si * numpy.sqrt(252))/100

print sig

#Black-Sholes tries to find the speculative difference
def BlackSholes():
    S = float(raw_input("Stock Price: "))
    X = float(raw_input("Strike Price: "))
    if S > X:
        print("In the Money")
        print ("Intrinsic Value is")
        print S-X

    t = float(raw_input("Expiration Time: "))
    T = t/365

    r = float(raw_input("Risk Free Interest: "))

    log = numpy.log(S/X)
    d1 = ((log)+(r+((sig)*(sig))/2)*(T))/(sig*(numpy.sqrt(T)))
    print d1
    d2 = d1 - (sig*(numpy.sqrt(T)))
    print d2
    c = S*(norm.cdf(d1)) - X*(numpy.exp((-r)*T))*(norm.cdf(d2))
    p = X*(numpy.exp((-r)*T))*(norm.cdf(-d2)) - S*(norm.cdf(-d1))
    print ('The Black-Sholes Option Price')
    print ('Call Price')
    print c
    print ('Put Price')
    print p
    C = raw_input("Would you like to continue? y/n")
    if C is 'y':
        for i in range(50, 350, 50):
            z = X + i
            log = numpy.log(S/z)
            d1 = ((log)+(r+((sig)*(sig))/2)*(T))/(sig*(numpy.sqrt(T)))
            d2 = d1 - (sig*(numpy.sqrt(T)))
            c = S*(norm.cdf(d1)) - z*(numpy.exp((-r)*T))*(norm.cdf(d2))
            p = z*(numpy.exp((-r)*T))*(norm.cdf(-d2)) - S*(norm.cdf(-d1))
            print ('Call Price at ', z)
            print c
            print ('Put Price at ', z)
            print p

BlackSholes()    




