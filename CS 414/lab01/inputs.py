'''
This program runs the first lab.
These three lines, between triple quotes, are "comments".
Python ignores them; they're just there to help you, the programmer.
'''

# BTW, lines that begin with a hash-sign are also ignored

name = input('Whats your name? ')

print ("Hello, " + name + ", It is very nice to meet you!")

temp = input("Celsius? ")

temp = float(temp)

print (temp, "C is", (temp*1.8)+32, "F")

