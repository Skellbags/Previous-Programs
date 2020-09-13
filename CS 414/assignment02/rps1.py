'''
This program asks the user for r, p, or s,
once for player 1, and once for player 2.

It then determines who won the game of rock/paper/scissors
'''
print("Hello, and welcome to my Quartz, Parchment, and Shears (rock, paper, scissors) Game!\nI will prompt Player 1 for a move, then player 2, then tell you who won!(Use r, p, and s)")

#prompts
p1 = input("Player1's move: ")
p2 = input("Player2's move: ")

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
