'''
Takes a numerator and denominator from user
(using two calls to input()), and prints them
as a (possibly improper) fraction reduced to lowest terms.
'''

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return print(a)




def main():
    a = int(input('numerator? '))
    b = int(input('denominator? '))
    gcd(a,b)
    
if __name__ == '__main__':
    main()

#RS
