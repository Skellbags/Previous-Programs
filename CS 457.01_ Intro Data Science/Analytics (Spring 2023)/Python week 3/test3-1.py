#RJS1070 Python week 3
print("###PygLatin Converter:")
l = ['a','e','i','o','u']
t = 'how are you doing'
pyg = lambda w: w[1:]+w[0].lower()+"ay"
pygV = lambda w: w+"way"
print(" Regular:\n  ", end="")
[print(i,"",end="") for i in t.split(" ")]
print("\n Pyglatin:\n  ", end="")
for i in t.split(" "):
    if i[0] in l:
        print(pygV(i), end=" ")
    else:
        print(pyg(i), end=" ")
print(" ")


print("\n###Grader:")
blob = [("A+",97,4.0),("A",93,4.0),("A-",90,3.7),("B+",87,3.3),("B",83,3.0),("B-",80,2.7),("C+",76,2.4),("C",73,2.0),("C-",70,1.8)]
def grader(val):
    if type(val)==int:
        for it in range(0,len(blob)-1):
            if (val >= blob[it][1]):
                return blob[it][0]
            elif (val == blob[it][1]):
                return blob[it][0]
            elif (val <= 72):
                return blob[-1][0]
            elif val <= blob[it][1]:
                pass
            else:
                return blob[it][0]
    elif type(val)==str:
        for it in range(0,len(blob)-1):
            if (val == blob[it][0]): 
                return blob[it][2] 
            else:
                continue
    else:
        print("AHHHH")

def gradeCtl(filename):
    fi = open(filename, "r")
    grads = fi.read().strip('\n').split(",")
    fi.close()
    gradsC = []
    try:
        for i in grads:
            gradsC.append(int(i))
        tot = 0
        for i in gradsC:
            tot += i
        totF = int(round(tot/len(gradsC),0))
        print(' In:  ',filename+'\n  Original:\n  ', gradsC,'\n  Avg in #:', totF,'\n  Letter:', grader(totF))
    except:
        for i in grads:
            gradsC.append(grader(i))
        tot = 0
        for i in gradsC:
            tot += i
        totF = tot/len(gradsC)
        print('\n In: ',filename+'\n  Original:\n  ', grads,'\n  GPA:', round(totF,2))  


#test3.scores:
#70,80,90,100,100,90,80,70
gradeCtl('test3.scores')
#test3.letters:
#A,A-,B+,B
gradeCtl('test3.letter')

print("\n###Multi to Dict:")
mls = """
apples 5
bananas 6
carrots 7
"""
mls2 = """
apples 5
bananas 6
carrots 7
apples 10000000000000000000
bananas 2000000000000000000
carrots 3000000000000000000
"""
def mlsToDict(im):
    m = {}
    f = im.strip('\n').split('\n')
    [m.update([(i.split(" "))]) for i in f]
    return m
print(" mls = \n'''",mls.strip('\n')+"'''")
print("  dict(mls) = ",mlsToDict(mls))
print("\n mls2 = \n'''",mls2.strip('\n')+"'''")
print("  dict(mls2) = ",mlsToDict(mls2))
x, y = mlsToDict(mls), mlsToDict(mls2)
print('\nMLS items == MLS2 items is',x.items()==y.items())
print('\nMLS keys == MLS2 keys is',x.keys()==y.keys())

#EXTRAS
print("\n###Descriptive Values:")
def multi(l):
    mi,ma,ra= min(l), max(l), max(l)-min(l)
    me,med,mo = round(sum(l)/len(l),2), l[int(len(l)/2)],max(set(l), key=l.count)
    if len(l)%2==0:
        x = [l[int(len(l)/2)],l[int(len(l)/2)-1]]
        med = sum(x)/len(x)
    print("Min:{}, Max:{}, Range:{}\nMean:{}, Median:{}, Mode:{}".format(mi,ma,ra,me,med,mo))
    """
    mean, median, mode
    for i in l:
        if
    """
lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,1]
print('DS: ',lis)
multi(sorted(lis)) # Found most calculators online like to sort the list too

print("\n###Prime Numbers:")
def isPrime(num):
    for i in range(2, num):
        if num == 1:
            break
        if num%i == 0:
            return print(num,False)
    return print(num,True)
isPrime(1)
isPrime(2)
isPrime(3)
isPrime(5)
isPrime(9)
isPrime(8)

uge = {}
print("\n###OWL.txt:")
def load():
    fi = open('OWL.txt', "r")
    dis = fi.read().split("\n")
    fi.close()
    for i in dis:
        i2 = i.split(' ')
        k, v = i2[0].lower(), " ".join(i2[1:]) 
        uge.update([(k,v)])
load()
fin = lambda h: print(f'Word: {h}\n ',uge[h])
fin('maybe')
fin('yes')
fin('definition')
fin('speed')
fin('velocity')
