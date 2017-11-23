from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "http://quotes.yourdictionary.com/theme/marriage/"

response = urlopen(url).read()
soup = BeautifulSoup(response)

citati = []

for item in soup.findAll("p", attrs={"class": "quoteContent"}):
    print item.text
    citati.append(item)
    if len(citati) == 5:
        break





