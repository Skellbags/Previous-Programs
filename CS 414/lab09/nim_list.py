# 7: Do this last:
# Instead of 3 piles with 5 stones each,
# ask the user for the number of piles,
# and the number of stones per pile.

pile_sizes = []
count = 1
num_of_Piles = int(input("How many piles would you like"))
while True:
    num_of_Stones = int(input("Enter the number of stones for Pile"))
    pile_sizes.append(int(num_of_Stones))
    num_of_Piles -= 1
    count += 1
    if num_of_Piles == 0:
        break

player = 1

while True:
    # Print a line to separate this move from the previous move
    print ('\n' + '-' * 20)

    for index in range(len(pile_sizes)):
        print ('Pile', index+1, ':', pile_sizes[index], 'stones')


    print ('Player', player, 'is next.')

    # Prompt user for a pile, and do input validation
    while True:
        pile = int(input('which pile? '))
        if not (1 <= pile and pile >= num_of_Piles):
            print ('Invalid Input')
            continue
        else:
            if pile_sizes[pile-1] <= 0:
                print ('Pile ', pile_sizes[pile-1],' is empty.  Choose another pile.')
            else:
                break
    # Prompt user for number of stones, and do input validation
    while True:
        n_stones = int(input('Take how many stones? '))

        if n_stones == 0 or n_stones == "":
            print ('You MUST take some stones.')
        elif pile_sizes[pile-1] < n_stones:
            print ('There are only', pile_sizes[pile-1], 'stones in that pile.')
        else:
            break

    pile_sizes[pile-1] -= n_stones

    total_stones = sum(pile_sizes)

    # Did anybody win?
    if total_stones == 0:
        if player == 1:
            print ('Player 2 wins!')
        else:
            print ('Player 1 wins!')
        break


    player = 3 - player
