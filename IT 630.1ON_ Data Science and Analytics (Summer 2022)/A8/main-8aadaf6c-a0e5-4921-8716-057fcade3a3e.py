"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
A8 - 6/26/22 - Purpose:
    Plotting various Graphs based on file input
Note:
    $fs and $ext for file(s) and extention
Supported Files:
    in1.txt
    in2.txt
    in3.txt
    in4.txt
"""
fs=["in1", "in2", "in3", "in4"]
ext=".txt"

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
    
def endit(n,o):
    axs[n,o].grid(color='0.8', linestyle='-', linewidth=2)
    axs[n,o].scatter(x,y, c=was.labels_, cmap='rainbow')
    axs[n,o].scatter(was.cluster_centers_[:,0] ,was.cluster_centers_[:,1], color='black')
    axs[n,o].set_title('Data From: '+fs[ind], fontweight='bold')
    axs[n,o].set_xlabel('x-axis', fontweight='bold')
    axs[n,o].set_ylabel('y-axis', fontweight='bold')
    if(ind==2):
        axs[n,o].legend(loc="upper left")
    else:
        axs[n,o].legend()
        
if __name__ == "__main__":
    print("#### RJS1070 - IT 630 - A8 - 6/26/22 ####")
    print("############### Plott-in ################\n")
    
    fig, axs = plt.subplots(2, 2, figsize=(20,12), sharey=False)
    for ind in range(len(fs)):
        if ind==0
        data = pd.read_csv(fs[ind]+ext, header=None)
        x=[]
        y=[]
        for i in data.values:
            x.append(i.tolist()[0])
            y.append(i.tolist()[1])
        was = KMeans(n_clusters=2)
        was.fit(data)
        print("\n#########################################")
        print("Input File:  ", fs[ind])
        print("Data points: ", len(x))
        if ind==0:
            endit(0,0)
        elif ind==1:
            endit(0,1)
        elif ind==2:
            endit(1,0)
        else:
            endit(1,1)
    fig.tight_layout()
    plt.show()
"""
    in1, Linear Regression
        The few points on the graph are almost entirely linear, enforcing the fact that
        clustering is redundant on this data set.
    in2, Clusters(K-means)
        The second data set lacks any conformity to a linear function, so I could only
        deduce that K-means should probably be used. I tried to increase the cluster
        count, although I couldn't pin down a good value, that sorted all points evenly.
    in3, Linear Regression
        The third data set is incredibly dense and forms almost a spider web-like shape.
        This could go either way, however, I couldn't find any decernable groupings so
        linear regression would make the most sense.
    in4, Clusters
        The fourth data set has a large break in the center of the set, which could be
        considered for some sort of grouping, although the KMeans scikit-learn class places
        four of the points in the wrong grouping
"""    
