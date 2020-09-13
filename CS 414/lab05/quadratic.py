import sys

'''
Solve a quadratic equation
'''
print("Hello, and welcome to my quadratic equation calculator!/n You give me an A, B, and C, and ill give you the roots!")
while True:
    a = float(input('A? '))
    b = float(input('B? '))
    c = float(input('C? '))
    if a == 0 and b == 0 and c == 0:
        break
    else:
        d = b**2 - 4*a*c
        x = -b/(2*a)
        x1 = (-b - d**0.5)/(2*a)
        x2 = (-b + d**0.5)/(2*a)

        if d < 0:
            print("No Real Roots")
        elif d == 0:
            print("There is 1 root", x)
        else:
            print("There is 2 roots", round(x1, 3), "and", round(x2, 3))

#RS

