
pile1_size = 5
pile2_size = 5
pile3_size = 5
total = pile1_size + pile2_size + pile3_size
player_ID = 1

while True:
    print("#" * 50)
    print("Player", player_ID,"moves next")

    print ('Pile 1 has', pile1_size, 'stones', end = ", ")
    print ('Pile 2 has', pile2_size, 'stones', end = ", ")
    print ('Pile 3 has', pile3_size, 'stones')

    while True:
        try:
            stones_taken = int(input('Take how many stones? '))
            sub_Pile = int(input("From which Pile?"))
        except ValueError:
            print("That cannot be entered")
            continue
        if stones_taken <= 0:
            print("That cannot be entered")
            continue
        elif (sub_Pile == 1 and stones_taken > pile1_size) or (sub_Pile == 2 and stones_taken > pile2_size) or (sub_Pile == 3 and stones_taken > pile3_size):
            print("That cannot be entered")
            continue
        else:
            break

    
    if sub_Pile == 1:
        pile1_size -= stones_taken
    elif sub_Pile == 2:
        pile2_size -= stones_taken
    elif sub_Pile == 3:
        pile3_size -= stones_taken
    else:
        print("There is no pile with that number")

    if player_ID == 1:
        player_ID = 2
    else:
        player_ID = 1

    if total == 0:
        print("Player", player_ID,"Wins")
        break
