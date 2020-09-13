'''
Determines how many steps it takes for a positive integer number
to reach the value 1, making these transformations at each step:

* if the number is even, divide it by 2
* if it is odd, multiply by 3, and add 1 to it
'''
print("Hello, and welcome to my Collatz Calculator")
n = int(input('n? '))
count = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
        count += 1
    else:
        n = n * 3 + 1
        count += 1
print(count,"Transformations")

#RS
