'''
Verify Ramanujan's claim that 1729 is the sum of two cubes,
in two different ways:
  find a, b, c, d such that
     a**3 + b**3 == c**3 + d**3, and
     a, b are different from c, d

Method: write four for-loops, one inside the other:
   for a ...
       for b ...
           for c ...
               for d ...

This will cover all possible combinations.  When you find the claimed
a,b,c,d, you should stop looking.  Your job then is to find a way to
exit from a nested for-loop.
'''
a = 1
b = 1
c = 1
d = 1
count = 1729
for a in range(1,int(count**(1/3)+1)):
    for b in range(1,int(count**(1/3)+1)):
        for c in range(1,int(count**(1/3)+1)):
            for d in range(1,int(count**(1/3)+1)):
                
                if (a == b) or (b == c) or (c == d) or (a == d) or (d == b) or (a == c):
                    break
                aAndb = (a**3 + b**3)
                cAndd = (c**3 + d**3)
                if (a**3 + b**3) == (c**3 + d**3):
                    if (aAndb == count) and (cAndd == count):
                        print(a, "+", b, "and", c, "+", d," both equal", count, "!") 
#RS
