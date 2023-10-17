"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
C1 - 5/26/22 - Supported Files:
    input.txt
Purpose:
    Read in data files, and return a nested dictionary object
"""
def c1():
    peopleObj = open("input.txt", "r")
    lineArry = []
    drac = 0
    for line in peopleObj.readlines():
        print(line, end="")
        hold = line.split(",")
        templine = tuple(map(float, hold))
        lineArry.insert(drac,templine)
        drac +=1
    peopleObj.close()
    return lineArry
