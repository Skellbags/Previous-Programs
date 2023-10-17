"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
A5 - 6/15/22 - Purpose:
    Simple (X, Y) pair displaying function(s)
Note:
    None
Supported Files:
    input.txt
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from c1 import c1

def scatterShow():
    x, y = (zip(*c1()))
    line = plt.scatter(x, y, alpha=0.5)
    plt.text(0.51, 0.28, 'Here Is a best fit line', style='italic', fontsize = 15)
    plt.tight_layout()
    plt.subplots_adjust(left=2, right=4, bottom=2, top=4)
    plt.xticks(rotation = 90)
    a, b = map(float, np.polyfit(x, y, 1))
    test = list(x)
    ntest =[]
    drac = 0
    for i in test:
        ntest.insert(drac, a*i+b)
        drac += 1
    plt.plot(x, ntest, alpha=0.6)
    plt.show()
def scatterShow2():
    x, y = (zip(*c1()))
    line = plt.plot(x, y, '.r-', alpha=0.3)
    plt.text(0.51, 0.28, 'As you can see, this data is not sorted', style='italic', fontsize = 15)
    plt.tight_layout()
    plt.subplots_adjust(left=2, right=4, bottom=2, top=4)
    plt.xticks(rotation = 90)
    plt.show()
if __name__ == "__main__":
    scatterShow()
    scatterShow2()
    """
    print("#### RJS1070 - IT 630 - A5 - 6/15/22 ####")
    print("########### Naive Bayes Test ###########\n")
    
    Hisoka = input("Please enter a valid Problem Letter(From A5.pdf):\n(a,b,c,d)").capitalize()
    print("###", Hisoka+ ":")
    while(Hisoka):
        
        print("#########################################")
        Hisoka = input("Another Problem Letter?(Or CR to quit):\n").capitalize()
        if (bool(Hisoka)):
            continue
        else:
            break
    print("Exiting!")
    """
    