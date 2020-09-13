'''
CS414 Assignmen01
Your Name:Ryan J Skelly
'''

# Question 1: Wind Chill

#prompts
print("Hello! And welcome to my wind chill converter!")
Temp = float( input('Please enter the Temperature in degrees fahrenheit. ') )
Speed = float( input('Please enter the Wind Speed in miles per hour. ') )

#algorithm
Chill = (35.74 + (0.6215 * Temp) + ( (0.4275 * Temp) - 35.75)*(Speed ** 0.16))

#result
print("Results Just got back! With a wind speed of", Speed, "and a temperature of", Temp, ", your corresponding"
      " Wind chill would be", round(Chill, 2))

# Question 2: Check Order

#prompts
print("Hello! And welcome to my Order Checker! This program will check three different numbers and see if they are"
      " sorted(The first # should be the smallest #, and the third # should be the biggest #).")
x = float( input('The first #? ') )
y = float( input('The second #? ') )
z = float( input('The third #? ') )
#algorithm
if (x <= y) and (y <= z):
    sort = True
else:
    sort = False
#result
if (sort == True):
    print("Those Numbers are sorted!")
else:
    print("Those Numbers are !!!NOT!!! sorted!")
    
# Question 3: Print your Initials

#result
print("Here is My intials, RJS, which stands for Ryan Joseph Skelly.")
print("***** *****  ****")
print("*   *   *   *    ")
print("*   *   *   *    ")
print("*****   *    *** ")
print("*       *       *")
print("**      *       *")
print("* *   * *       *")
print("*  *  ***   **** ")

# Question 4: Print a rectangle

#prompts
print("Hello! And welcome to my rectangle drawing tool! Enter the width, and the height to draw a rectangle.")
width = int( input('Desired width? ') )
height = int( input('Desired height? ') )

#algorithm
print(("X" * (width)),("\n"+"X" * width )* (height-1))

#RS
