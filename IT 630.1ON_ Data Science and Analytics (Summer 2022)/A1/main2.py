"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
C3 - 5/28/22 - Purpose:
    Web Scraper that grabs and outputs of Items found on the Craigslist website
        return all items in a CSV file(ID,LINK,TIME,TITLE,PLACE) w/o SPAM,
    Now with Inputs!
Note:
    None
Supported Files:
    None
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
print("#### RJS1070 - IT 630 - A1 - 5/30/22 ####")
print("############# Craig's Arry2 #############\n")
cont = True
while(cont):
    wrong = 1
    while(wrong==1):
        try:
            st = input("Howdy! and Welcome to Craig's Array!!! The primitive craigslist scraping CLI!!\nFirst off, by which state would you like to query for?\n (Local Name/ Boston, NH, Toledo, VT, etc.):")
            url = "https://{}.craigslist.org/search/zip".format(st.lower())
            url2 = "https://{}.craigslist.org/search/zip?s=120".format(st.lower())
            url3 = "https://{}.craigslist.org/search/zip?s=240".format(st.lower())
            html = urlopen(url)
            soup = BeautifulSoup(html, "html.parser")
            print("loaded", url)
            html2 = urlopen(url2)
            soup2 = BeautifulSoup(html2, "html.parser")
            print("loaded", url2)
            html3 = urlopen(url3)
            soup3 = BeautifulSoup(html3, "html.parser")
            print("loaded", url3, "\n")
            wrong = 0
        except:
            print("Seems as though the input you gave for the state wasn't valid, Restarting!\n(Note: this may take some time to get right, in the meantime, here are all possible values you could have selected!)")
            htmlParams = urlopen("https://www.craigslist.org/about/sites")
            soupParams = BeautifulSoup(htmlParams, "html.parser")
            justCols = soupParams.find("div", class_="colmask").findAll("div")
            for i in justCols:
                justRows = i.findAll("a")
                for j in justRows:
                    print(j.get("href").split(".")[0].replace("https://", ""))
                
    beans = input("Any title parameters?\n (string to search):")
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
                if((res[1] == "result-info") or ("span" in res[4])):
                    return
                else:
                    if(beans in res[3]):
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
            vlad +=1
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
    cont = False
    cont = bool(input("Would you like to continue?\n (Any Value/ press enter to exit):"))
    if cont == True:
        continue
    else:
        break
    
    
