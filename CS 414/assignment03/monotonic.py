'''
Determines if three numbers form a monotonic or non-monotonic sequence
'''
print("Hello, and welcome to my Monotonic Tester. You give me 3 Values and Ill tell you whether theyre monotonic or not")
x = float(input('First? '))
y = float(input('Second? '))
z = float(input('Third? '))

if (x>=y>=z) or (x<=y<=z):
    print("Monotonic")
else:
    print("Non-Monotonic")

#RS
