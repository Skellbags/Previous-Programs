'''
Simulates a lunar landing
'''

# Here, initialize the ship's mass, fuel, height, velocity
print("    __\n",
"   \ \_____\n",
"###[==_____>\n",
"   /_/      __\n",
"            \ \_____\n",
"         ###[==_____>\n",
"            /_/\n")
print("Hello! and welcome to my lunar landing simulation\nGood Luck and Have Fun!")
H = 1000
V = 0
Mfuel = 1000
Vnozzle = 100
Mship = 1000
# Then, enter a loop:
valid = True
while valid == True:
    # Show the user the current status of the ship
    print("Height:", "{:>7}".format(int(H)), "Speed:", "{:>7}".format(int(V)), "Fuel:", "{:>7}".format(Mfuel))
    # Ask the user for amount to burn
    burn_reply = input('Amount of fuel to burn? ')
    if burn_reply == "" or " ":
        print("Oops!  That was not a valid number.  Try again...")
        burn_reply = input('Amount of fuel to burn? ')
        Mburn = float(burn_reply)
    else:
        pass
    Mburn = float(burn_reply)

    # Check if that amount can be burnt
    if Mburn > Mfuel:
        print("Oops!  That was not a valid number.  Try again...")
        burn_reply = input('Amount of fuel to burn? ')
        Mburn = float(burn_reply)
    elif Mburn < 0:
        print("Oops!  That was not a valid number.  Try again...")
        
        burn_reply = input('Amount of fuel to burn? ')
        Mburn = float(burn_reply)
    else:
        Mburn = float(burn_reply)
        Mfuel -= Mburn
        
    # Update the ship's mass
    g = 1.6
    Pfuel = Mburn * Vnozzle
    V = V - Pfuel / (Mship + Mfuel) + g
    H = H - V
    # Check if you have landed OK
    if H == 0:
        print("Height:", "{:>7}".format(int(H)), "Speed:", "{:>7}".format(int(V)), "Fuel:", "{:>7}".format(Mfuel))
        print ('Tranquility base.  The Eagle has landed')
        break
    else:
        pass

    # Check if you have crashed
    if H < 0:
        print("Height:", "{:>7}".format(int(H)), "Speed:", "{:>7}".format(int(V)), "Fuel:", "{:>7}".format(Mfuel))
        print ('You crashed!')
        break
    else:
        pass
print("############  GOOD GAME   #############")

#RS
