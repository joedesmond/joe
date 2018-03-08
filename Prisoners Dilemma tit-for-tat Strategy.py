import string
import time
import random
from random import randint

global e, p, i

print("Prisoners Dilemma: Tit for Tat")
print("")

i = 0
p = 0
e = 0



x1 = raw_input("C or D")
y1 = randint(0,1)

if x1 == "C" and y1 == 0:
    i = i-1
    p = p-1
    print(i, p)

if x1 == "C" and y1 == 1:
    i = i-10
    p = p
    print(i, p)

if x1 == "D" and y1 == 0:
    i = i
    p = p-10
    print(i, p)

if x1 == "D" and y1 == 1:
    i = i-6
    p = p-6
    print(i, p)

print("")


x2 = raw_input("C or D")
y2 = x1

if x2 == "C" and y2 == "C":
    i = i-1
    p = p-1
    print(i, p)

if x2 == "C" and y2 == "D":
    i = i-10
    p = p
    print(i, p)

if x2 == "D" and y2 == "C":
    i = i
    p = p-10
    print(i, p)

if x2 == "D" and y2 == "D":
    i = i-6
    p = p-6
    print(i, p)

print("")
    
    
x3 = raw_input("C or D")
y3 = x2

if x3 == "C" and y3 == "C":
    i = i-1
    p = p-1
    print(i, p)

if x3 == "C" and y3 == "D":
    i = i-10
    p = p
    print(i, p)

if x3 == "D" and y3 == "C":
    i = i
    p = p-10
    print(i, p)

if x3 == "D" and y3 == "D":
    i = i-6
    p = p-6
    print(i, p)

print("")


x4 = raw_input("C or D")
y4 = x3

if x4 == "C" and y4 == "C":
    i = i-1
    p = p-1
    print(i, p)

if x4 == "C" and y4 == "D":
    i = i-10
    p = p
    print(i, p)

if x4 == "D" and y4 == "C":
    i = i
    p = p-10
    print(i, p)

if x4 == "D" and y4 == "D":
    i = i-6
    p = p-6
    print(i, p)

print("")

x5 = raw_input("C or D")
y5 = x4

if x5 == "C" and y5 == "C":
    i = i-1
    p = p-1
    print(i, p)

if x5 == "C" and y5 == "D":
    i = i-10
    p = p
    print(i, p)

if x5 == "D" and y5 == "C":
    i = i
    p = p-10
    print(i, p)

if x5 == "D" and y5 == "D":
    i = i-6
    p = p-6
    print(i, p)

print("")

print("final Score:")
print("")

if i < p:
    print(i, p)
    print("")
    print ("you Lose")
    time.sleep(100)
    

if i > p:
    print(i, p)
    print("")
    print ("You Win")
    time.sleep(100)
    

if i == p:
    print(i, p)
    print("")
    print ("You Draw")
    time.sleep(100)
    

        




