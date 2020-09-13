'''
This program is like rps1.py, but it generates
'r', 'p', or 's' depending on a random value.

It then determines who won the game of rock/paper/scissors
'''

import random
print("Hello, and welcome to my Quartz, Parchment, and Shears (rock, paper, scissors) Game!\nYou will be playing against me! Make your move and I will tell you if you, or I won!\nSince I made the game... Im Player 1!(Use r, p, and s)")

#prompts
p1 = random.choice( ["r", "p", "s"] )
p2 = input("Your Move?: ")

#algorithm
if p1 == p2:
    print("!!!TIE!!!")
elif p1 == "r" and p2 == "p":
    print("!!!PLAYER 2 WINS!!!")
elif p1 == "s" and p2 == "p":
    print("!!!PLAYER 1 WINS!!!")
elif p1 == "r" and p2 == "s":
    print("!!!PLAYER 2 WINS!!!")
elif p1 == "p" and p2 == "s":
    print("!!!PLAYER 2 WINS!!!")
elif p1 == "p" and p2 == "r":
    print("!!!PLAYER 2 WINS!!!")
elif p1 == "s" and p2 == "r":
    print("!!!PLAYER 2 WINS!!!")
else:
    print("!!!ERROR!!! INVALID SYNTAX")

#RS


