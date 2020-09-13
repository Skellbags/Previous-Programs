'''
Flip two coins 100 times, and count how many times
they come up the same, and how many times different.
'''

import random
n = 100
n_same = 0
n_different = 0
while n > 0:
    flip1 = random.randint(1,2)
    flip2 = random.randint(1,2)
    if flip1 == flip2:
        n_same += 1
    else:
        n_different += 1
    n -= 1
print("Here are the Results!")
print("# of same Flips:", n_same)
print("# of different Flips:", n_different)

#RS
