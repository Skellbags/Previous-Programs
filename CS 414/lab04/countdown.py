'''
Get a number from the user, and count down to 1.
'''
import time
print("Hello, welcome to my countdown timer! /nIll ask you for seconds and count them down for you!")
n = int( input('How many Seconds? ') )

while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
print("!!DONE!!")

#RS
