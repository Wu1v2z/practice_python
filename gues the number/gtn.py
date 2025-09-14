import random
import sys
import time 


num = random.randint(1.0, 100.0)


while True:
    gues_num = float(input('Gues the number'))

    if num < gues_num :
        print('Number is less')
    elif num > gues_num :
        print('Number is bigger')
    else :
        print('You are winner!') 