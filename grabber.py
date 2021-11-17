# coding=utf-8

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
from collections import defaultdict
data=defaultdict(list)

def calculatePriceFromIndiaMart(itemtype,company,url):
    page = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    total = soup.get_text()
    filtered=[]
    price=[]
    if(not bool(data)):
        if(itemtype not in data.keys()):
            data[itemtype]=[]

    for i in total.split():
        if(i.__contains__("₹")):
            priceStr=i.split('₹')[1]
            if(not priceStr.__contains__(",")):
                price.append(int(float(priceStr[0:len(priceStr)-1])))
                

    for item in price:
        if(item > 0 and item <=500):
            filtered.append(item)

    data[itemtype].append(
        {
            "company": company,
            "average-cost": sum(filtered)/len(filtered),
            "maximum-cost": max(filtered)
        }
    )
    with open('data.json', 'w+') as outfile:
        json.dump(data, outfile,indent=4)

file1 = open('input.csv', 'r')
Lines = file1.readlines()

for line in Lines:
    if "," in line:
        calculatePriceFromIndiaMart(line.split(",")[0],line.split(",")[1],line.split(",")[2])

with open('data.json') as json_file:
    output = json.load(json_file)
    print(json.dumps(output, indent=4, sort_keys=True))
