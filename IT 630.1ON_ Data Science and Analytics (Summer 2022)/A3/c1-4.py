"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
C1 - 5/26/22 - Supported Files:
    Ratings.csv
    People.csv
Purpose:
    Read in data files, and return a nested dictionary object
"""
def c1():
    peopleObj = open("People.csv", "r")
    lineArry = []
    drac = 0
    
    for line in peopleObj.readlines():
        templineArry = line.split(",")
        lineArry.insert(drac, templineArry[0])
        drac += 1
    peopleObj.close()
    
    
    trueLineDict = {}
    drac = 0
    for i in lineArry:
        lineDict = {}
        ratingsObj = open("Ratings.csv", "r")
        for line in ratingsObj.readlines():
            splitRat = line.split(",")
            tempDict = { splitRat[0] : float(splitRat[2].replace("\n", ""))}
            if splitRat[1] == i :
                lineDict.update(tempDict)
        trueLineDict.update({ lineArry[drac] : lineDict})
        drac +=1
    return trueLineDict
