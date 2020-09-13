'''
Flip a coin 100 times, and count the number of heads
and tails.
'''

import random
n = 100
heads = 0
tails = 0
while n > 0:
    flip = random.randint(1,2)
    if flip == 1:
        heads += 1
    else:
        tails += 1
    n -= 1
print("Here are the Results!")
print("# of heads", heads)
print("# of tails", tails)

#RS
