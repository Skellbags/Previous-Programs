'''
This program extends rps2.py.
Instead of generating r, p, or s ONCE, it does
so several times.  It then counts how many
times each player won, and how many tied games occurred.
'''

import random
print("Hello, and welcome to my Quartz, Parchment, and Shears (rock, paper, scissors) Game!\nYou will be playing against me! Make your move and I will tell you if you, or I won!\nSince I made the game... Im Player 1!(Use r, p, and s)")

n_games = int( input('But before we start, How many games would you like to play? ') )

#prompts

p1w = 0
p2w = 0
tie = 0
#algorithm
for i in range(n_games):
    p1 = random.choice( ["r", "p", "s"] )
    p2 = random.choice( ["r", "p", "s"] )
    if p1 == p2:
        tie += int(1)
    elif p1 == "r" and p2 == "p":
        p2w += int(1)
    elif p1 == "s" and p2 == "p":
        p1w += int(1)
    elif p1 == "r" and p2 == "s":
        p1w += int(1)
    elif p1 == "p" and p2 == "s":
        p2w += int(1)
    elif p1 == "p" and p2 == "r":
        p1w += int(1)
    elif p1 == "s" and p2 == "r":
        p2w += int(1)
    else:
        print("!!!ERROR!!! INVALID SYNTAX")
        break

print("Good Game! Well Played! Here are our Results!")
print("I won", p1w,"games!")
print("You won", p2w,"games!")
print("We tied", tie,"games!")
print("I won", round(((p1w)/n_games)*100,2 ), "% of the games!")
print("You won", round(((p2w)/n_games)*100,2 ), "% of the games!")
print("We tied", round(((tie)/n_games)*100,2 ), "% of the games!")

#RS
