import string 
import random
from random import randint

print("Prisoners Dilemma: Random")

i = 0
p = 0
e = 0

def random():

    global e, p, i

    x = raw_input("C or D")
    y = randint(0,1)

    if x == "C" and y == 0:
        i = i-1
        p = p-1
        print(i)

    if x == "C" and y == 1:
        i = i-10
        p = p
        print(i)

    if x == "D" and y == 0:
        i = i
        p = p-10
        print(i)

    if x == "D" and y == 1:
        i = i-6
        p = p-6
        print(i)

    e = e+1

    if e < 5:
        random()

    if e == 5:

        if i < p:
            print(i, p)
            print ("you Lose")

        else:
            print(i, p)
            print ("You Win")

random()

