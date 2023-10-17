"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
C8 - 6/28/22 - Purpose:
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
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt

def plot1():
    customer_data = pd.read_csv('dogs.csv')
    data = customer_data.iloc[:, 1:2].values
    cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
    cluster.fit_predict(data)
    plt.figure(figsize=(10, 7))
    plt.title("Dog Breed Dendrogram")
    dend = shc.dendrogram(shc.linkage(data, method='ward'))

    

def plot2():
    plt.show()
    customer_data = pd.read_csv('dogs.csv').to_numpy()
    x = customer_data[:, 1]
    y = customer_data[:, 2]
    data = np.stack((x, y), axis=1)
    cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
    cluster.fit_predict(data)
    plt.title("Dog Breed Scatter Plot")
    plt.scatter(x,y, c=cluster.labels_, cmap='rainbow')
    plt.show()
    
if __name__ == "__main__":
    print("#### RJS1070 - IT 630 - C8 - 6/28/22 ####")
    print("############ Scikit-Learning ############\n")
    plot1()
    print("First Plot done")
    plot2()
    print("Second Plot done")
