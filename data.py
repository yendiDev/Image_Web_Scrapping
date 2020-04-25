from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

data = []
try:
    html = urlopen("https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/")
    bsObject = BeautifulSoup(html.read(), features='xml')
    data = bsObject.findAll("td", {"class":"font-weight: bold; font-size:16px; text-align:left; padding-left:5px; padding-top:10px; padding-bottom:10px"})
    print(data)
except URLError as e:
    print(e)