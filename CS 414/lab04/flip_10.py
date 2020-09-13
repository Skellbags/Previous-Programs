'''
Flip a coin 10 times.
'''

import random
n = 10
heads = 0
tails = 0
while n > 0:
    flip = random.randint(1,2)
    if flip == 1:
        print("Heads")
        heads += 1
    else:
        print("Tails")
        tails += 1
    n -= 1
print("Here are the Results!")
print("# of heads", heads)
print("# of tails", tails)

#RS
