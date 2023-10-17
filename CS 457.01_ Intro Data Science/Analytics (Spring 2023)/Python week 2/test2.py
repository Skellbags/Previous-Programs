#RJS1070 Python week 2
l = ['a','e','i','o','u']
t = "Never gonna give you up \
Never gonna let you down \
Never gonna run around and desert you \
Never gonna make you cry \
Never gonna say goodbye \
Never gonna tell a lie and hurt you".split(" ")
pyg = lambda w: w[1:]+w[0].lower()+"ay"
pygV = lambda w: w+"way"
print(" Regular:")
[print(i,"",end="") for i in t]
print("\n\n Pyglatin:")
for i in t:
    if i[0] in l:
        print(pygV(i), end=" ")
    else:
        print(pyg(i), end=" ")

def kfcToKFC(temp):
    if temp[-1].lower() == "c": return str((float(temp[:-1])*9/5)-32)+"F"
    elif temp[-1].lower() == "f": return str((float(temp[:-1])-32)*5/9)+"C"
    elif temp[-1].lower() == "k":
        return " ".join([str((1.8*(float(temp[:-1])-237.15))+32)+"F", "and\
", kfcToKFC(str((1.8*(float(temp[:-1])-237.15))+32)+"F")])

v = ["0C", "0F", "0K"]
print("\n\n kfcToKFC(I):\n Where I is 0 Celsius(C->F), Freezing Point(F->C), and \
Absolute Zero(K->F & C)")
[print(kfcToKFC(i)) for i in v]

blob = [("A+",97,4.0),("A",93,4.0),("A-",90,3.7),("B+",87,3.3),("B",83,3.0),("B-",80,2.7),("C+",76,2.4),("C",73,2.0),("C-",70,1.8)]


def grader(val):
    if type(val)==int:
        for it in range(0,len(blob)-1):
            if (val >= blob[it][1]):
                print(val, "->",blob[it][0])
                return
            elif (val == blob[it][1]):
                print(val, "->",blob[it][0])
                return
            elif (val <= 72):
                print(val, "->",blob[-1][0])
                return
            elif val <= blob[it][1]:
                pass
            else:
                print(val, "->",blob[it][0])
    elif type(val)==str:
        for it in range(0,len(blob)-1):
            if (val == blob[it][0]):
                print(val, "->",blob[it][2])
                return
            else:
                continue

print("\n Scores:")
for i in range(70, 101, 2):
    print(str(grader(i)).strip("None")+"", end="")
print("\n Letters:")
for some in range(0,len(blob)-1):
    print(str(grader(blob[some][0])).strip("None")+"", end="")
print("\n\n Palindrome:")
def p(b):
    [print("|"+b.upper()+"|", end=" ") if b == b[::-1] else print(b, end=" ")]
pal = "kayak\
 deified\
 rotator\
 repaper\
 deed\
 peep\
 wow\
 noon\
 civic\
 racecar\
 level\
 mom".split(" ")
for i in t:
    pal.append(i)
for i in pal:
    p(i)
