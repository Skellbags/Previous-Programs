"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
A3 - 6/30/22 - Purpose:
    Use Euclidean and Manhattan formulas to find Neighbors, via the Minkowski 
    Distance formula
    Find linear correlation of bordering nodes with the pearson formula
    Find Cosine similarity of bordering nodes with the cosine coefficent
Note:
    None
Supported Files:
    None
"""
from c1 import c1
import recommendation as r
def printe(x,y,z):
    for i in x:
        print ("### ", i[y],"->", i[z])
names = c1()
if __name__ == "__main__":
    print("#### RJS1070 - IT 630 - A3 - 6/30/22 ####")
    print("############### FlixFindr ##############\n#########'Now Case Insensitive!'########")
    Hisoka = input("Enter a Name:\n").lower().capitalize()
    while(Hisoka):
        """
        print("# Recommendations using Manhattan Formula")
        distances = r.computeNearestNeighbor (1, Hisoka, names)
        print("## Nearest Neighbors of {}".format(Hisoka))
        printe(distances, 1, 0)
        recommend = r.recommend(1, Hisoka, names)
        print("## Recommendations for {}: ".format(Hisoka))
        printe(recommend, 0, 1)
        
        print("# Recommendations using Euclidean Formula")
        distances = r.computeNearestNeighbor (2, Hisoka, names)
        print("## Nearest Neighbors of {}".format(Hisoka))
        printe(distances, 1, 0)
        recommend = r.recommend(1, Hisoka, names)
        print("## Recommendations for {}: ".format(Hisoka))
        printe(recommend, 0, 1)
        """
        print("# Recommendations using Pearson Formula")
        distances = r.computeNearestNeighbor (2, Hisoka, names, 1)
        print("## Nearest Neighbors of {}".format(Hisoka))
        printe(distances, 1, 0)
        recommend = r.recommend(1, Hisoka, names, 1)
        print("## Recommendations for {}: ".format(Hisoka))
        printe(recommend, 0, 1)
        print("# Recommendations using Cosine Coefficient Formula")
        distances = r.computeNearestNeighbor (1, Hisoka, names, 0, 1)
        print("## Nearest Neighbors of {}".format(Hisoka))
        printe(distances, 1, 0)
        recommend = r.recommend(1, Hisoka, names, 0, 1)
        print("## Recommendations for {}: ".format(Hisoka))
        printe(recommend, 0, 1)
        print("\n#########################################\n")
        Hisoka = input("Enter a Name(Or CR to quit):\n").lower().capitalize()
        if (bool(Hisoka)):
            continue
        else:
            break
    print("Exiting!")

