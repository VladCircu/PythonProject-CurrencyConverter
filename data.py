import xml.etree.ElementTree as ET
import urllib.request
from bs4 import BeautifulSoup

def data():
    url_curs_valutar = "https://www.bnr.ro/nbrfxrates.xml"
    req = urllib.request.urlopen(url_curs_valutar)
    xml = BeautifulSoup(req,'xml')

    currency = {}
    for item in xml.findAll('Rate'):
            s = ""
            currency[s.join(item.get_attribute_list("currency"))] = float(item.text)

    return currency

# data()