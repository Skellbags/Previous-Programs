#Hey Prof. Narayan,
#Im leaving these here just for testing purposes to make your life easier!
#If you're running into issues where my program yells "Missing lat/long info" at 
#you, just replace these variables with your own, or shoot me an email @ 
#rjs1070@wildcats.unh.edu
freeGeoIPAPIkey = "zrHGog7ztrOhApFRTWz4HnfUGjuz88cTMcOr19Rw"
googleMapsAPI = "AIzaSyB4UXqkXpyV13otRZa5-nH3s9COWxCbFK8"


"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
A2 - 6/2/22 - Purpose:
    Web Scraper that grabs IP addresses from the editing history of a 
    wikipedia page and displays geographical information for that IP addr
Note:
    None
Supported Files:
    None
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import requests

def printer(x): 
    if (type(x) == BSresultSet):
        for i in x:
            tempArry.append(printer(i)) #Recursive call
    elif ((type(x) == BStag)):
        idStr = x.prettify().split("\n")[1].split("=")[-1].strip(">").strip('"')
        if(idStr[0] == "S"):
            return idStr.split("/")[1]
    elif(type(x) == type(finArry)):
        tra = []
        for i in x:
            if (i != None):
                try:
                    maybe = tra.index(i)
                except:
                    finArry.append(i)
                    tra.append(i)
 
def geoIpHelper(x):
    resp = requests.get("https://api.ipbase.com/v1/json/"+x+"?apikey="+freeGeoIPAPIkey)
    ret = json.loads(resp.text)
    try:
        print("#########################################")
        try:
            holArry = []
            holArry.append(str(ret['ip']))
            holArry.append(str(ret['country_name']))
            holArry.append(str(ret['region_name']))
            holArry.append(str(ret['city']))
            holArry.append( "https://maps.googleapis.com/maps/api/staticmap?zoom=13&size=600x600&maptype=roadmap&markers=color:red%7C"+str(ret['latitude'])+","+str(ret['longitude'])+"&key="+googleMapsAPI)
            f = open("out.csv", "a")
            f.write(",".join(holArry[i])+"\n")
            f.close()
            print("#", end="")
        except:
            print("!! File No Print !!")
        twas = "# IP: "+str(ret['ip'])
        brilig = " # Country: "+str(ret['country_name'])
        andSlithy = " # Region: "+str(ret['region_name'])
        toves = " # City: "+str(ret['city'])
        did = "\n"+"# Link: https://maps.googleapis.com/maps/api/staticmap?zoom=13&size=600x600&maptype=roadmap&markers=color:red%7C"
        gyre = str(ret['latitude'])+","
        andGimble = str(ret['longitude'])+"&key="+googleMapsAPI
        inTheWabe = twas + brilig + andSlithy
        allMimsy = toves + did + gyre
        were = inTheWabe + allMimsy + andGimble
        return were+"\n"
    except KeyError:
        return "!! Missing Latitude/Longitude Information !!"



print("#### RJS1070 - IT 630 - A2 - 6/2/22 ####")
print("############### WikiSniff ##############\n")
htmlParams = urlopen("https://en.wikipedia.org/w/index.php?title=Dynamic_Host_Configuration_Protocol&offset=&limit=100&action=history")
soup = BeautifulSoup(htmlParams, "html.parser")
justCols = soup.findAll("span", class_="history-user")
BSresultSet = type(soup.findAll("meta")) 
BStag = type(soup.find("div"))
tempArry = []
finArry = []
printer(justCols)
printer(tempArry)
for i in finArry:
    print(geoIpHelper(i))
print("\n#########################################")