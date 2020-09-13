def is_right():
    
    a = int(input("A?"))
    b = int(input("B?"))
    c = int(input("C?"))
    if ((a**2 + b**2) == (c**2)) or ((a**2 + c**2) == (b**2)) or ((b**2 + c**2) == (a**2)):
        print("Right")
    else:
        print("Not Right")


def main():
    is_right()
    
if __name__ == '__main__':
    main()

#RS
