'''
Prints out a table of Fahrenheit and Celsius temperatures,
in steps of 8 degrees C, from -40C to +40C
'''
# Write your program below this line:
#   Start with celsius = -40,
#   Create a loop
#   Increment the temperature by 8 each time.
print("Celsius Fahrenheit")
for n in range(-40,48,8):
    print("{:>7}   {:<7}".format(n, (n * 9//5) + 32))

#RS
