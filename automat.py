
from komisje.models import *
import urllib
from bs4 import BeautifulSoup
import sys


wyb_url = "http://prezydent2010.pkw.gov.pl/PZT/PL/WYN/W/index.htm"
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
woj = [woj[0]]

for w in woj:
    wm = Wojewodztwo(name=w[0])
    wm.save()
    powi = parse_page(w[1])
    for p in powi:
        print p[0]
        pm = Powiat(name=p[0], woj=wm)
        pm.save()
        gmin = []
        if p[0].endswith("m."):
            gmin = [p]
        else:            
            gmin = parse_page(p[1])
        for g in gmin:
            gm = Gmina(name=g[0], powiat=pm)
            gm.save()    
            okr = parse_page(g[1])
            for o in okr:
                om = Okreg(name=o[0], gmina=gm, karty=0, wyborcy=0)
                om.save()
            sys.stdout.write('.')
        print p[0], " done"


