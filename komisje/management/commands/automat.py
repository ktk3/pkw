from django.core.management.base import BaseCommand
from komisje.models import *
import urllib
from bs4 import BeautifulSoup
import sys


wyb_url = "http://prezydent2010.pkw.gov.pl/PZT/PL/WYN/W/index.htm"
base_url = wyb_url.rsplit('/',1)[0]

def open_conn(url):
    filehandle = urllib.urlopen(url)
    html_doc = filehandle.read()
    soup = BeautifulSoup(html_doc)
    soup = soup.find(id="s0")
    soup_tbody = soup.find_all("tbody")
    soup = soup_tbody[0]
    soup_tr = soup.find_all("tr")
    return soup_tr


def parse_page(url):
    soup_tr = open_conn(url)
    tab =[]
    for tr in soup_tr:
        a = tr.find("a")
        tab.append([a.string, base_url + "/" + a["href"]])  
    return tab

def parse_zagr_page(url, pm):
    soup_tr = open_conn(url)
    okr = []
    for tr in soup_tr:
        a = tr.find("a")
        if not a:
            a = tr.find("td", { "class":"col2al" })
            a = a.string[2:]
            gm = Gmina(name=a, powiat=pm)
            gm.save()    
            for o in okr:
                om = Okreg(name=o, gmina=gm, karty=0, wyborcy=0)
                om.save()
            okr[:] = []
        else:
            okr.append(a.string)  
class Command(BaseCommand):

    help = "Populates db with data"




    def handle(self, **options):
        woj = parse_page(wyb_url)

        for w in woj:
            if w[0] != "mazowieckie":
                continue
            wm = Wojewodztwo(name=w[0])
            wm.save()
            powi = parse_page(w[1])
            for p in powi:
                self.stdout.write(p[0])
                pm = Powiat(name=p[0], woj=wm)
                pm.save()
                gmin = []
                if p[0] == "Zagranica": 
                    zagr = parse_zagr_page(p[1], pm)
                else:
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
                        self.stdout.write('.')
                self.stdout.write(" done\n")

        self.stdout.write( "ALL DONE\n")
