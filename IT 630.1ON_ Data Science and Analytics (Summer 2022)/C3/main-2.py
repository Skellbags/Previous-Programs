"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
C3 - 5/28/22 - Purpose:
    Web Scraper that grabs and outputs of Items found on the Navigation website
        return all singular prices and the sum
Note:
    None
Supported Files:
    None
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://cs.unh.edu/~anarayan/scraping/Navigation.html"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
BSresultSet = type(soup.findAll("td")) 
BStag = type(soup.find("td"))
finArry = []
def printer(x): 
    drac = 0
    tempArry = []
    if (type(x) == BSresultSet):
        for i in x:
            if (drac == 4):
                finArry.append(tempArry)
                tempArry = []
                drac = 0
                tempArry.append(printer(i)) #Recursive call
                drac += 1
            else:
                tempArry.append(printer(i)) #Recursive call
                drac += 1
    elif ((type(x) == BStag)):
        try:
            return x.get_text().strip("\n\r").strip("$").replace(",", "")
        except:
            return x.get_text().strip("\n")       
            
print("#### RJS1070 - IT 630 - C3 - 5/28/22 ####")
print("############ Navigation.html ############\n")
printer(soup.findAll("td"))
tot = []
print("  Items:")
for i in range(len(finArry)):
    print("   "+finArry[i][0]," ==> ", finArry[i][2])
    tot.append(float(finArry[i][2]))
print("  Total:", sum(tot),"\n")
print("#########################################")
    
    
