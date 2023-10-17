"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
C4 - 6/4/22 - Purpose:
    Use Euclidean and Manhattan formulas to find Neighbors, via the Minkowski 
    Distance formula
Note:
    None
Supported Files:
    None
"""
from c1 import c1
import recommendation as r

names = c1()
inname = "Dan"
if __name__ == "__main__":
    print("#### RJS1070 - IT 630 - C4 - 6/4/22 ####")
    print("############### FlixFindr ##############\n#########'Now Case Insensitive!'########")
    Hisoka = input("Enter a Name:\n").lower().capitalize()
    while(Hisoka):
        print("# Recommendations using Manhattan Formula")
        distances = r.computeNearestNeighbor (1, Hisoka, names)
        print("## Nearest Neighbors of {}".format(Hisoka))
        for item in distances:
            print ("### ",item[1],"->", item[0])
        recommend = r.recommend(1, Hisoka, names)
        print("## Recommendations for {}: ".format(Hisoka))
        for item in recommend:
            print("### ",item[0], "->", item[1])
        print("# Recommendations using Euclidean Formula")
        distances = r.computeNearestNeighbor (2, Hisoka, names)
        print("## Nearest Neighbors of {}".format(Hisoka))
        for item in distances:
            print ("### ",item[1],"->", item[0])
        recommend = r.recommend(1, Hisoka, names)
        print("## Recommendations for {}: ".format(Hisoka))
        for item in recommend:
            print("### ",item[0], "->", item[1]) 
        print("\n#########################################\n")
        Hisoka = input("Enter a Name(Or CR to quit):\n").lower().capitalize()
        if (bool(Hisoka)):
            continue
        else:
            break
    print("Exiting!")

