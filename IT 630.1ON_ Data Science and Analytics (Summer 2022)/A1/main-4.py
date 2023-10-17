"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
C3 - 5/28/22 - Purpose:
    Web Scraper that grabs and outputs of Items found on the Craigslist website
        return all items in a CSV file(ID,LINK,TIME,TITLE,PLACE) w/o SPAM
Note:
    None
Supported Files:
    None
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
print("#### RJS1070 - IT 630 - A1 - 5/30/22 ####")
print("############# Craig's Array #############\n")

url = "https://nh.craigslist.org/search/zip"
url2 = "https://nh.craigslist.org/search/zip?s=120"
url3 = "https://nh.craigslist.org/search/zip?s=240"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
print("loaded", url)
html2 = urlopen(url2)
soup2 = BeautifulSoup(html2, "html.parser")
print("loaded", url2)
html3 = urlopen(url3)
soup3 = BeautifulSoup(html3, "html.parser")
print("loaded", url3, "\n")
BSresultSet = type(soup.findAll("meta")) 
BStag = type(soup.find("div"))
finArry = []
def printer(x): 
    if (type(x) == BSresultSet):
        for i in x:
            finArry.append(printer(i)) #Recursive call
    elif ((type(x) == BStag)):
        try:
            idStr = x.prettify().split("=")[2].split('"')[1] #print("ID:",x.prettify().split("=")[2].split('"')[1])
            linkStr = x.prettify().split("=")[5].split('"')[1] #print("LINK:",x.prettify().split("=")[5].split('"')[1])
            timeStr = x.prettify().split("=")[11].split('"')[1] #print("TIME:",x.prettify().split("=")[11].split('"')[1])
            titleStr = x.prettify().split("=")[17].split("\n")[1].strip(" ") #print("TITLE:",x.prettify().split("=")[17].split("\n")[1].strip(" "))
            placeStr = x.prettify().split("=")[19].split("\n")[1].strip(" ").strip("(").strip(")") #print("PLACE:",x.prettify().split("=")[19].split("\n")[1].strip(" ").strip("(").strip(")"))
            res = [idStr, linkStr, timeStr, titleStr, placeStr]
            #print(res)
            if((res[1] == "result-info") or "span" in res[4]): #INPUT VALIDATION: if picture didn't exist, if location wasn't provided, if title had a ("), or (')
                return
            else:
                return res 
        except:
            pass
            

printer(soup.findAll("li", class_="result-row"))
printer(soup2.findAll("li", class_="result-row"))
printer(soup3.findAll("li", class_="result-row"))
print(" Items:")
vlad = 0
for i in range(len(finArry)):
    if(finArry[i] == None):
        vlad +=1 #fail tally
        continue
    print("   "+finArry[i][3].lower(),"/", finArry[i][4].lower(), "/", finArry[i][2])
    try:
        f = open("out.csv", "a") #had to put in try ctlstruct because one item had an emoji and I wasn't trying to print the unicode char
        f.write(",".join(finArry[i])+"\n")
        f.close()
    except:
        continue
    
print("|| Total Items Indexed:", len(finArry), "|| Valid(!SPAM/ERR) Items Indexed:", len(finArry)-vlad, "||")
print("#########################################")
print("\nNOTE: Hey Prof. Narayan,\n As a preface, I designed this program to be a scraper of the NH Craig's List site, and that it should function psuedo-dynamically. When implementing CSV functionality, I thought to design this program such that it could be run once a day and keep a running tally of all items indexed(Thus, the output file is never deleted). After doing a once over of the directions, I couldn't quite pin down a specific line refering to the management of output files, so I hope this will suffice! Also while I was at it, I hope you don't mind but I changed the output to include the place and the ID for quick querying of webpages/items.\n\n Format of output: ID,LINK,TIME,TITLE,PLACE")
    
    
