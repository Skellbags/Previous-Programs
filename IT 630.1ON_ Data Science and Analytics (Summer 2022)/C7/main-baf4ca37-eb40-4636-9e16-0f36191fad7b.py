"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
C7 - 6/28/22 - Purpose:
    Use the dogs data set to demonstrate scikit-learn's
    Hierarchical/Agglomerative Clustering
Note:
    LATE SUBMISSION
Supported Files:
    dogs.csv
"""
import pandas as pd
import numpy as np
import sklearn as sklearn
import matplotlib.pyplot as plt

def plot1():
    frank= [82, 75, 86, 63, 90, 73, 88]
    alex= [91, 92, 80, 73, 83, 91, 71]


    fig, ax = plt.subplots(tight_layout=True)
    temp = np.arange(7)
    bw = 0.35
    th = 0.8

    bar1 = plt.bar(temp, frank, bw, alpha=th, color='r', label='Frank')
    bar2 = plt.bar(temp + bw, alex, bw, alpha=th, color='g', label='Alex')

    plt.ylabel('Scores')
    plt.title('Grading: Frank VS Alex')
    plt.xticks((temp + bw/2), ("A1", "A2", "A3", "A4", "A5", "Midterm", "Final"), rotation = 45)
    plt.legend()
    print("First Plot done")
    plt.tight_layout()
    plt.show()
        

    

def plot2():
    ds = np.array([1,1,2,3,3,5,7,8,9,10,10,11,11,13,13,15,16,17,18,18,18,19,20,21,21,23,24,24,25,25,25,25,26,26,26,27,27,27,27,27,29,30,30,31,33,34,34,34,35,36,36,37,37,38,38,39,40,41,41,42,43,44,45,45,46,47,48,48,49,50,51,52,53,54,55,55,56,57,58,60,61,63,64,65,66,68,70,71,72,74,75,77,81,83,84,87,89,90,90,91])
    fig, axs = plt.subplots(2, 1, sharey=True, tight_layout=True)
    fig.suptitle('50 Bins VS 100 Bins')
    #50
    axs[0].hist(ds, bins=50)
    axs[0].set_title('Histogram | bins = 50')
    axs[0].set_ylabel('Frequencies')
    #100
    axs[1].hist(ds, bins=100)
    axs[1].set_title('Histogram | bins = 100')
    axs[1].set_ylabel('Frequencies')
    
    plt.show()
    
if __name__ == "__main__":
    print("#### RJS1070 - IT 630 - C7 - 6/28/22 ####")
    print("############ Scikit-Learning ############\n")
    plot1()
    plot2()
    
    
