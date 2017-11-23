from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Game_of_Thrones"

wiki_url_start = urlopen(url).read()
wiki_html_start = BeautifulSoup(wiki_url_start)

seznam_sezon = wiki_html_start.find("table", attrs={"class": "wikitable"})

for link in seznam_sezon.findAll("a"):
        if link.string == "Season":
            sezona_html = urlopen(url + link["href"]).read()
            sezona_soup = BeautifulSoup(sezona_html)

            epizode = sezona_soup.findAll("tr", attrs={"class", "vevent"})
            for st_gledalci in epizode:
                st_gledalci = epizode.findAll("td")[-1].text

                sum(st_gledalci)

print "Vse epizode serij Game of the Thrones imajo skupno %s milijonov gledalcev" % (sum)


