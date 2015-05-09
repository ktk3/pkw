
#from komisje.models import *
import urllib
from bs4 import BeautifulSoup


wyb_url = "http://prezydent2010.pkw.gov.pl/PZT/PL/WYN/W/020000.htm"
base_url = wyb_url.rsplit('/',1)[0]

def parse_page(url):
    filehandle = urllib.urlopen(url)
    html_doc = filehandle.read()

    soup = BeautifulSoup(html_doc)
    soup = soup.find(id="s0")
    soup_tbody = soup.find_all("tbody")
    soup = soup_tbody[0]
    soup_tr = soup.find_all("tr")

    tab =[]
    for tr in soup_tr:
        a = tr.find("a")
        tab.append([a.string, base_url + "/" + a["href"]])
    return tab

woj = parse_page(wyb_url)

for p in woj:
#    Wojewodztwo(name=p[0]).save()
    print p[0]
print ""
for p in woj:
    print p[1]
