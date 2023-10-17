"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
A5 - 6/15/22 - Purpose:
    B| Classify Votes.txt file to determine:
        1) Alternate ‘y’ and ‘n’ votes starting with ‘y’
        2) 4 ‘y’ votes followed by 4 ‘n’ notes followed by 8 ‘n’ votes
        3) All ‘n’ votes
        4) All ‘y’ votes
        5) 3 ‘n’ votes followed by 3 ‘y’ votes followed by 3 ‘n’ votes followed by 1 ‘y’ vote followed
        by 6 ‘n’ votes
    C| Classify pimaSmall.txt to determine:
        linear independence vs dependence of subject fields Via Bayes Density Classifier
    D| Classify dermatologydata.txt to determine:
        Effectiveness of the Bayes Density Classifier at choosing accurate predictions
Note:
    ####################
    README.txt SUPPLEMENT
    ####################
    When prompted select problem to run based on the corresponding letter on A5.pdf(I decided to include problem A because it was a given, Check A for no run)
    
    Inplace methods can be imported by:
        
        from main import <PROB#(lowercase)>Prob as ProblemNumberModule(Or anything else)
    
    Just drag all supported files into the local dir to run
Supported Files:
    naiveBayesBasic.py
    naiveBayeDensity.py
    a:
        i-01-salary.txt
    b:
        votes.txt
    c:
        pimaSmall.txt
    d:
        dermatologydata.txt
          Information About DataSet provided in dermatologynames.txt, and at http://archive.ics.uci.edu/ml/datasets/Dermatology
"""
from naiveBayesBasic import *
from naiveBayesDensity import Classifier as cCompile
import math

def aProb():
    """COMMENT OUT DOWN BELOW IF YOU DONT DECIDE TO ADD IN i-01-salary.txt"""
    c = Classifier("i-01-salary.txt","attr\tattr\tattr\tattr\tnum\tclass")
    """"""
    print("Prior Probabilities:")
    print(c.prior)
    print("\nConditional Probabilities:")
    print(c.conditional)
    print("")
    print("Classify somebody with the following attributes:")
    print("Reason: 'health'; Exercise level: 'moderate'; Motivation: 'moderate'; Salary:'0' Tech Devices: 'no'")
    print("Likely to buy: ", c.classify(['health', 'moderate', 'moderate', '0', 'no']))
    print()
    print("Reason: 'health'; Exercise level: 'sedentary'; Motivation: 'moderate'; Salary:'100' Tech Devices: 'no'")
    print("Likely to buy: ", c.classify(['health', 'sedentary', 'moderate', '100', 'no']))
    
def bProb():
    c = Classifier("votes.txt","class\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr\tattr")
    print("Prior Probabilities:")
    print(c.prior)
    print("\nConditional Probabilities:")
    print(c.conditional)
    print("#########################################\n")
    print("Classify somebody with the following attributes:\n")
    print("1) Alternate ‘y’ and ‘n’ votes starting with ‘y’\nVoting:", c.classify(['y', 'n', 'y', 'n','y', 'n','y', 'n','y', 'n','y', 'n','y', 'n','y', 'n']))
    print()
    print("2) 4 ‘y’ votes followed by 4 ‘n’ notes followed by 8 ‘n’ votes\nVoting:", c.classify(['y', 'y', 'y', 'y', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']))
    print()
    print("3) All ‘n’ votes\nVoting:", c.classify(['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']))
    print()
    print("4) All ‘y’ votes\nVoting:", c.classify(['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']))
    print()
    print("5) 3 ‘n’ votes followed by 3 ‘y’ votes followed by 3 ‘n’ votes followed by 1 ‘y’ vote followed \nby 6 ‘n’ votes\nVoting:", c.classify(['n', 'n', 'n', 'y', 'y', 'y', 'n', 'n', 'n', 'y', 'n', 'n', 'n', 'n', 'n', 'n']))
    print()



def cProb():
    def cPrint(p):
        if (p == "1"):
            print("Likely")
        else:
            print("Unlikely")
    c = cCompile("pimaSmall.txt","num\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tclass")
    print("Probabilities:")
    for key in sorted(c.prior):
        print("%s: %s" % (key, c.prior[key]))
    print("#########################################\n")
    print("Classify somebody with the following attributes:\n")
    """
    Reasoning:
        For a baseline person, I went and queried all of the global averages for the different fields, 
        each subsequent test would have a higher value for the field being tested(Independent/Dependent Testing)
        Each of the Values was found by googling a value, if given a range for the value I got the average
        It could be that every single source is completely made up ... ¯\_(ツ)_/¯
    """
    print("Baseline Pseudo-Human\nLikeliness:", end="")
    cPrint(c.classify([], [2.5, 100, 70, 18.7, 26.55, 17.5, 0.5 ,36.6]))
    print()
    print("1) Pregnancy Increase\nLikeliness:", end="")
    cPrint(c.classify([], [7.5, 100, 70, 18.7, 26.55, 17.5, 0.5 ,36.6]))
    print()
    print("2) Plasma Glucose Increase\nLikeliness:", end="")
    cPrint(c.classify([], [2.5, 200, 70, 18.7, 26.55, 17.5, 0.5 ,36.6]))
    print()
    print("3) Blood Pressure Increase\nLikeliness:", end="")
    cPrint(c.classify([], [2.5, 100, 100, 18.7, 26.55, 17.5, 0.5 ,36.6]))
    print()
    print("4) Tricep Thickness Increase\nLikeliness:", end="")
    cPrint(c.classify([], [2.5, 100, 70, 22, 26.55, 17.5, 0.5 ,36.6]))
    print()
    print("5) Serum Insulin Increase\nLikeliness:", end="")
    cPrint(c.classify([], [2.5, 100, 70, 18.7, 26.7, 17.5, 0.5 ,36.6]))
    print()
    print("6) BMI Increase\nLikeliness:", end="")
    cPrint(c.classify([], [2.5, 100, 70, 18.7, 26.55, 24, 0.5 ,36.6]))
    print()
    print("7) Diabetes Ancestory Increase\nLikeliness:", end="")
    cPrint(c.classify([], [2.5, 100, 70, 18.7, 26.55, 17.5, 1 ,36.6]))
    print()
    print("8) Age Increase\nLikeliness:", end="")
    cPrint(c.classify([], [2.5, 100, 70, 18.7, 26.55, 17.5, 0.5 ,72]))
    print()
    print("Extreme Pseudo-Human\nLikeliness:", end="")
    cPrint(c.classify([], [7,160,54,32,175,30.5,1,39]))
    print()
    

        
def dProb():
    def dPrint(p):
        if (p == "1"):
            return "psoriasis"
        elif (p == "2"):
            return "seboreic dermatitis"
        elif (p == "3"):
            return "lichen planus"
        elif (p == "4"):
            return "pityriasis rosea"
        elif (p == "5"):
            return "cronic dermatitis"
        else:
            return "pityriasis rubra pilaris"
    c = cCompile("dermatologydata.txt","num\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tnum\tclass")
    print("Probabilities:")
    for key in sorted(c.prior):
        print("%s: %s" % (key, c.prior[key]))
    print("#########################################\n")
    print("Classify somebody with the following attributes:\n")
    print("Baseline Pseudo-Human(All Zeros/No Skin Conditions)\nLikeliness:", end="")
    print(dPrint(c.classify([], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35])))
    print()
    print("Extreme Pseudo-Human(All Ones/All Skin Conditions, Severity:Minor)\nMost Likely:", end="")
    print(dPrint(c.classify([], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 35])))
    print()
    print("Extreme Pseudo-Human(All Twos/All Skin Conditions, Severity:Moderate)\nMost Likely:", end="")
    print(dPrint(c.classify([], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 35])))
    print()
    print("Extreme Pseudo-Human(All Threes/All Skin Conditions, Severity:Severe)\nMost Likely:", end="")
    print(dPrint(c.classify([], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 35])))
    print()
    print("Psoriasis Pseudo-Patient\nMost Likely:", end="")
    print(dPrint(c.classify([], [3, 2, 1, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 35])))
    print()
    print("seboreic dermatitis Pseudo-Patient\nMost Likely:", end="")
    print(dPrint(c.classify([], [2, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 35])))
    print()
    print("lichen planus Pseudo-Patient\nMost Likely:", end="")
    print(dPrint(c.classify([], [2, 1, 1, 1, 1, 2, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 2, 1, 1, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 3, 3, 35])))
    print()
    print("pityriasis rosea Pseudo-Patient\nMost Likely:", end="")
    print(dPrint(c.classify([], [1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 11])))
    print()
    print("cronic dermatitis Pseudo-Patient\nMost Likely:", end="")
    print(dPrint(c.classify([], [0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 35])))
    print()
    print("pityriasis rubra pilaris Pseudo-Patient\nMost Likely:", end="")
    print(dPrint(c.classify([], [2, 1, 1, 1, 0, 0, 2, 0, 3, 2, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 35])))
    print()
    print("#########################################\n")
    print("Note: All Pseudo-Patients were chose at random and given a base age.\nTherefore, the level of effectivness of the Bayes Density Classifier on this set of data can be \napproximated by seeing the correlaion of the Pseudo-Patients actual diagnosis VS the Most Likely \nDiagnosis\n")

if __name__ == "__main__":
    print("#### RJS1070 - IT 630 - A5 - 6/15/22 ####")
    print("########### Naive Bayes Test ###########\n")
    
    Hisoka = input("Please enter a valid Problem Letter(From A5.pdf):\n(a,b,c,d)").capitalize()
    print("###", Hisoka+ ":")
    while(Hisoka):
        if(Hisoka == "A"):
            aProb()
            print("#########################################")
        elif(Hisoka == "B"):
            bProb()
            print("#########################################")
        elif(Hisoka == "C"):
            cProb()
            print("#########################################")
        elif(Hisoka == "D"):
            dProb()
            print("#########################################")
        Hisoka = input("Another Problem Letter?(Or CR to quit):\n").capitalize()
        if (bool(Hisoka)):
            continue
        else:
            break
    print("Exiting!")
