'''
Random walk.  Drunkard starts in middle, and moves left-right at random.
Each time he reaches a cell, bump the count there.
'''
import random

STREET_LENGTH = 15
visit_count = [0] * STREET_LENGTH
drunk = 7
# make a for-loop that runs 100 times

# inside it, initialize position to 7, then
# enter a while-loop, that runs until position goes off the low or high end.
# At each iteration in the while-loop, get a random value, and
# increment or decrement position, with 50/50 probability.
# Add 1 to the visit_count at that position

for i in range(1000):
    drunk = 7
    while True:
            rOrl = random.randint(1,2)
            if (drunk == -1) or (drunk == 15):
                break
            if rOrl == 1:
                visit_count[drunk] += 1
                drunk += 1
            else:
                visit_count[drunk] += 1
                drunk -= 1

print(visit_count) 

#RS
