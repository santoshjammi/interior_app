# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import json
from collections import defaultdict
data = defaultdict(list)


def getStringsFromURL(url):
    page = urlopen(Request(url))
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


def calculatePriceFromIndiaMart(itemtype, company, url):
    #url = "https://dir.indiamart.com/search.mp?ss=centuryply+block+plywood+board&prdsrc=1&src=as-rcnt%3Apos%3D1%3Acat%3D-2%3Amcat%3D-2"
    # page = urlopen(url)
    # html = page.read().decode("utf-8")
    # soup = BeautifulSoup(html, "html.parser")
    total = getStringsFromURL(url)
    filtered = []
    price = []
    if (not bool(data)):
        # if(len(data.keys())==0):
        #    data[itemtype]=[]
        if (itemtype not in data.keys()):
            data[itemtype] = []

    for i in total.split():
        if (i.__contains__("₹")):
            priceStr = i.split('₹')[1]
            if (not priceStr.__contains__(",")):
                price.append(int(float(priceStr[0:len(priceStr)-1])))

    for item in price:
        if (item > 0 and item <= 5000):
            filtered.append(item)
    # print(filtered)
    data[itemtype].append(
        {
            "company": company,
            "average-cost": sum(filtered)/len(filtered),
            "maximum-cost": max(filtered)
        }
    )
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)
    #print("Average is : "+str(sum(filtered)/len(filtered)))
    #print("Maximum is : "+str(max(filtered)))
    # print(soup.find_all("img"))


# calculatePriceFromIndiaMart(
#     "plywood", "century", "https://dir.indiamart.com/search.mp?ss=centuryply+block+plywood+board&prdsrc=1&src=as-rcnt%3Apos%3D1%3Acat%3D-2%3Amcat%3D-2")
# calculatePriceFromIndiaMart(
#     "plywood", "austin", "https://dir.indiamart.com/search.mp?ss=austin+plywood+19mm&mcatid=181108&catid=209&prdsrc=1&src=as-popular%3Akwd%3Daustinpl%3Apos%3D3%3Acat%3D-2%3Amcat%3D-2")
# calculatePriceFromIndiaMart(
#     "plywood", "kitply", "https://dir.indiamart.com/search.mp?ss=kitply+vista+mr+and+bwr+grade+plywood&src=as-default%3Akwd%3Dkitply%3Apos%3D8%3Acat%3D209%3Amcat%3D181110&prdsrc=1&mcatid=181110&catid=209")
# calculatePriceFromIndiaMart(
#     "plywood", "sarda", "https://dir.indiamart.com/search.mp?ss=sarda+plywood&mcatid=1794&catid=209&prdsrc=1")
# calculatePriceFromIndiaMart(
#     "plywood", "greenply", "https://dir.indiamart.com/search.mp?ss=greenply+plywood&mcatid=181112&catid=209&prdsrc=1")
# calculatePriceFromIndiaMart(
#     "plywood", "alishan", "https://dir.indiamart.com/search.mp?ss=greenply+plywood&mcatid=181112&catid=209&prdsrc=1")

# # channels
# #
# calculatePriceFromIndiaMart("drawchannels", "hettich",
#                             "https://dir.indiamart.com/search.mp?ss=hettich+slides&mcatid=193459&catid=209&prdsrc=1&src=as-popular%3Akwd%3Dhettichs%3Apos%3D3%3Acat%3D-2%3Amcat%3D-2")
# calculatePriceFromIndiaMart(
#     "drawchannels", "olive", "https://dir.indiamart.com/search.mp?ss=olive+telescopic+channels&mcatid=26871&catid=812&prdsrc=1&src=as-popular%3Akwd%3Dolivechannels%3Apos%3D1%3Acat%3D-2%3Amcat%3D-2")


# calculatePriceFromIndiaMart("softclose_drawchannels", "multibrand",
#                             "https://dir.indiamart.com/search.mp?ss=olive+telescopic+channels&mcatid=26871&catid=812&prdsrc=1&src=as-popular%3Akwd%3Dolivechannels%3Apos%3D1%3Acat%3D-2%3Amcat%3D-2")

# # soft close hinges

# calculatePriceFromIndiaMart("softclosehinges", "hettich",
#                             "https://dir.indiamart.com/search.mp?ss=hettich%20softclose%20hinges&no_sugg=1")
# calculatePriceFromIndiaMart("softclosehinges", "olive",
#                             "https://dir.indiamart.com/search.mp?ss=olive%20softclose%20hinges&no_sugg=1")
# calculatePriceFromIndiaMart("softclosehinges", "hafele_multiBrand",
#                             "https://dir.indiamart.com/search.mp?ss=hafele%20softclose%20hinges&no_sugg=1")

# # wardrobe channels
# calculatePriceFromIndiaMart("wardrobe_channels", "hafele",
#                             "https://dir.indiamart.com/search.mp?ss=hafele+wardrobe+channel&mcatid=73909&catid=812&prdsrc=1&src=as-popular%3Akwd%3Dwardrobechannels%3Apos%3D1%3Acat%3D-2%3Amcat%3D-2")

#
# mine = getStringsFromURL(
#     "https://dir.indiamart.com/search.mp?ss=centuryply+block+plywood+board&prdsrc=1&src=as-rcnt%3Apos%3D1%3Acat%3D-2%3Amcat%3D-2")
# print(mine)

f = open("input.csv", "r")
for line in f.readlines():
    if ',' in line:
        print(line)
        calculatePriceFromIndiaMart(line.split(
            ',')[0], line.split(',')[1], line.split(',')[2])
print(f.readlines())


with open('data.json') as json_file:
    output = json.load(json_file)
    #print(json.dumps(output, indent=4, sort_keys=True))
    # for p in output["plywood"]:
    #    print(p)
