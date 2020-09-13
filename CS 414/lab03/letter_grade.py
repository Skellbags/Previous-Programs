'''
Convert a numerical score into a letter grade.
'''

score = float(input('Numerical score? '))

# Here, write a big if - elif - elif ... - else statement
# with a print() in each block.
if score>=94.0:
    print("congrats an", score,"is an A")
elif score>=90.0:
    print("congrats an", score,"is an A-")
elif score>=87.0:
    print("congrats an", score,"is an B+")
elif score>=84.0:
    print("congrats an", score,"is an B")
elif score>=80.0:
    print("congrats an", score,"is an B-")
elif score>=77.0:
    print("congrats an", score,"is an C+")
elif score>=74.0:
    print("congrats an", score,"is an C")
elif score>=70.0:
    print("congrats an", score,"is an C-")
elif score>=67.0:
    print("congrats an", score,"is an D+")
elif score>=64.0:
    print("congrats an", score,"is an D")
elif score>=60.0:
    print("congrats an", score,"is an D-")
else:
    print("That sucks", score,"is a failing grade")

#RS
