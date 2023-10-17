"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
C2 - 5/27/22 - Purpose:
    Web Scraper that grabs and outputs HTML tags formatted neatly
Note:
    Just to be clear, this was listed under the Isotope Analysis 
    tab in the Departments and Programs directory.
    Figured it'd be good lipsum
    URL: https://www.unh.edu/node/26
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.unh.edu/research/welcome-university-instrumentation-center/uic-affiliated-instruments/mass-spectrometer-elemental-analyzer-geovision-solution"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
BSresultSet = type(soup.findAll("a")) 
BStag = type(soup.find("a"))
def printer(x): 
    if (type(x) == BSresultSet):
        for i in x:
            printer(i) #Recursive call
    elif ((type(x) == BStag)):
        try:
            if (x.get_text().replace(" ", "").strip("\n") != ""): 
                print("     "+x.get_text().strip("\n") +"  ===>  "+ x.get("href"))
        except:
            if (x.get_text().replace(" ", "").strip("\n") != ""): 
                print("     "+x.get_text().strip("\n"))
    """On my test site, there was a and h2 tags that had a single space
    for its text content. For uniformity, Ive added extra if statem. however it
    adds to overall runtime, if statement can be replaced with regular print 
    line for optimized run"""            
            
print("#### TITLE ####")
printer(soup.title)
print("#### H1 ####")
printer(soup.findAll("h1"))
print("#### H2 ####")
printer(soup.findAll("h2"))
print("#### H3 ####")
printer(soup.findAll("h3"))
print("#### H4 ####")
printer(soup.findAll("h4"))
print("#### H5 ####")
printer(soup.findAll("h5"))
print("#### H6 ####")
printer(soup.findAll("h6"))
print("#### A ####")
printer(soup.findAll("a"))
