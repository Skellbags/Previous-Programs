def pi_approx():
    
    terms = int(input("How Many Terms of PI?"))
    final = 0
    count = 0
    sign = -1
    secterm = 1
    
    for x in range(terms-1):
        x += 1
        x = 1 /((x+2)+ count)
        count += 1
        secterm += (x * sign)
        sign *= -1
    final = 4 * secterm
    return print(final)


def main():
    pi_approx()
    
if __name__ == '__main__':
    main()

#RS

"""
actual  x  operations        secterm
*+ 1/1  /0 / 0 + 1           /1
- 1/3  /1 / 1 - 0.3333      / 0.6666
+ 1/5  /2 / 0.6666 + 0.2    / 0.8666
- 1/7  /3 / 0.8666 - 0.1428 / 0.7238
+ 1/9  /4 / 0.7238 + 0.1111 / 0.8349

- 1/11 /5 / 0.8349 - 0.0909 / 0.744

"""


