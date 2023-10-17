#!/usr/bin/python3
#Testing problems RJS1070@wildcats.unh.edu
def mealCalc(meal_cost, tax_rate, tip_rate):
    return meal_cost + meal_cost*tax_rate + meal_cost*tip_rate

def cToF(celcius):
    return (celcius*9/5)+32

def compoundInt(p, r, n, t):
    return round(p*( 1 + (r/n))**(n*t),2)

def distCalc(x1, y1, x2, y2):
    ls, rs= x2 - x1, y2 - y1
    tot = ls**2 + rs**2
    return tot**(1/2)

def sToHMS(secs):
    c = secs//3600, (secs%3600)//60, (secs%3600)%60 #H, M, S
    return c

def change(price, paidAmount):
    due = paidAmount-price
    l, n= [20,10,5,1,0.25,0.1,0.05,0.01],[price, paidAmount, due]
    for i in l:
        n.append(due//i)
        due%=i
    if round(due,2) == 0.01:
        n[-1] +=1
    if n[-1] >= 5:
        n[-2]+=1
        n[-1]-=5
    return n

print("mealCalc(70, 0.09, 0.20):\n    ",mealCalc(70, 0.09, 0.20))
print("\ncToF(0):\n    ", cToF(0))
print("\ncToF(32):\n    ", cToF(32))
print("\ncompountInt(1000, 0.1, 4, 5):\n    ", compoundInt(1000, 0.1, 4, 5))
print("\ndistCalc(1,1,-1,-1):\n    ",distCalc(1,1,-1,-1))
print("\nsToHMS(86399):\n    ", "h: {} m: {} s: {}".format(*sToHMS(86399)))
print("\nchange(63.59,100):\n    Price: {}  Paid: {}\n    Due: {}\
\n\n    Twenties: {}\n    Tens: {}\n    Fives: {}\n    Ones: {}\
\n    Quarters: {}\n    Dimes: {}\n    Nickels: {}\n    Pennies: {}".format(*change(63.60,100)))

