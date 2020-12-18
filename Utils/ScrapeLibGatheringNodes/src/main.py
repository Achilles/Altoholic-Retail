'''
Created on 18/12/2020

@author: teelo
'''
from bs4 import BeautifulSoup
from selenium import webdriver
import re

browser = webdriver.Firefox()
previousName = ""
results = "LibStub('LibGatheringNodes-1.0').enUS = {\n"


url = "https://www.wowhead.com/objects/mineral-veins#0+1+5"
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')
data = soup.find_all("tbody", {"class":"clickable"})[0]


for tr in data.find_all('tr'):
    firstone = tr.find_all("td")[0].find_all("a")[0]
    name = firstone.get_text()
    if previousName != name:
        href = firstone.get("href")
        href = re.search("[^\d+](\d+)[^\d+]", href).group(1)
        empty = True
        thisResult = ""
        thisResult += '\t["'
        thisResult += name
        thisResult += '"] = \t\t {'
        
        browser.get("https://www.wowhead.com/object=" + href + "/")
        soup2 = BeautifulSoup(browser.page_source, 'html.parser')
        
        data2 = soup2.find_all("tbody", {"class":"clickable"})
        if len(data2) > 0:
            data2 = data2[0]
            for tr2 in data2.find_all('tr'):
                namecolumn = tr2.find_all("td")[2].find_all("a")[0]
                typecolumn = tr2.find_all("td")
                if len(typecolumn) >= 10:
                    typecolumn = typecolumn[9].find_all("a")[0]
                    if typecolumn.get_text() == "Metal & Stone":
                        empty = False
                        thisResult += re.search("[^\d+](\d+)[^\d+]", namecolumn.get("href")).group(1)
                        thisResult += ", "
        
        thisResult += '},\n'
        
        if not empty:
            previousName = name
            results += thisResult


url = "https://www.wowhead.com/objects/mineral-veins#100+1+5"
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

data = soup.find_all("tbody", {"class":"clickable"})[0]
for tr in data.find_all('tr'):
    firstone = tr.find_all("td")[0].find_all("a")[0]
    name = firstone.get_text()
    if previousName != name:
        href = firstone.get("href")
        href = re.search("[^\d+](\d+)[^\d+]", href).group(1)
        empty = True
        thisResult = ""
        thisResult += '\t["'
        thisResult += name
        thisResult += '"] = \t\t {'
        
        browser.get("https://www.wowhead.com/object=" + href + "/")
        soup2 = BeautifulSoup(browser.page_source, 'html.parser')
        
        data2 = soup2.find_all("tbody", {"class":"clickable"})
        if len(data2) > 0:
            data2 = data2[0]
            for tr2 in data2.find_all('tr'):
                namecolumn = tr2.find_all("td")[2].find_all("a")[0]
                typecolumn = tr2.find_all("td")
                if len(typecolumn) >= 10:
                    typecolumn = typecolumn[9].find_all("a")[0]
                    if typecolumn.get_text() == "Metal & Stone":
                        empty = False
                        thisResult += re.search("[^\d+](\d+)[^\d+]", namecolumn.get("href")).group(1)
                        thisResult += ", "
        
        thisResult += '},\n'
        
        if not empty:
            previousName = name
            results += thisResult


url = "https://www.wowhead.com/objects/mineral-veins#200+1+5"
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

data = soup.find_all("tbody", {"class":"clickable"})[0]
for tr in data.find_all('tr'):
    firstone = tr.find_all("td")[0].find_all("a")[0]
    name = firstone.get_text()
    if previousName != name:
        href = firstone.get("href")
        href = re.search("[^\d+](\d+)[^\d+]", href).group(1)
        empty = True
        thisResult = ""
        thisResult += '\t["'
        thisResult += name
        thisResult += '"] = \t\t {'
        
        browser.get("https://www.wowhead.com/object=" + href + "/")
        soup2 = BeautifulSoup(browser.page_source, 'html.parser')
        
        data2 = soup2.find_all("tbody", {"class":"clickable"})
        if len(data2) > 0:
            data2 = data2[0]
            for tr2 in data2.find_all('tr'):
                namecolumn = tr2.find_all("td")[2].find_all("a")[0]
                typecolumn = tr2.find_all("td")
                if len(typecolumn) >= 10:
                    typecolumn = typecolumn[9].find_all("a")[0]
                    if typecolumn.get_text() == "Metal & Stone":
                        empty = False
                        thisResult += re.search("[^\d+](\d+)[^\d+]", namecolumn.get("href")).group(1)
                        thisResult += ", "
        
        thisResult += '},\n'
        
        if not empty:
            previousName = name
            results += thisResult

url = "https://www.wowhead.com/objects/herbs#0+1+5"
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

data = soup.find_all("tbody", {"class":"clickable"})[0]
for tr in data.find_all('tr'):
    firstone = tr.find_all("td")[0].find_all("a")[0]
    name = firstone.get_text()
    if previousName != name:
        href = firstone.get("href")
        href = re.search("[^\d+](\d+)[^\d+]", href).group(1)
        empty = True
        thisResult = ""
        thisResult += '\t["'
        thisResult += name
        thisResult += '"] = \t\t {'
        
        browser.get("https://www.wowhead.com/object=" + href + "/")
        soup2 = BeautifulSoup(browser.page_source, 'html.parser')
        
        data2 = soup2.find_all("tbody", {"class":"clickable"})
        if len(data2) > 0:
            data2 = data2[0]
            for tr2 in data2.find_all('tr'):
                namecolumn = tr2.find_all("td")[2].find_all("a")[0]
                typecolumn = tr2.find_all("td")
                if len(typecolumn) >= 10:
                    typecolumn = typecolumn[9].find_all("a")[0]
                    if typecolumn.get_text() == "Herb":
                        empty = False
                        thisResult += re.search("[^\d+](\d+)[^\d+]", namecolumn.get("href")).group(1)
                        thisResult += ", "
        
        thisResult += '},\n'
        
        if not empty:
            previousName = name
            results += thisResult
            
url = "https://www.wowhead.com/objects/herbs#100+1+5"
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

data = soup.find_all("tbody", {"class":"clickable"})[0]
for tr in data.find_all('tr'):
    firstone = tr.find_all("td")[0].find_all("a")[0]
    name = firstone.get_text()
    if previousName != name:
        href = firstone.get("href")
        href = re.search("[^\d+](\d+)[^\d+]", href).group(1)
        empty = True
        thisResult = ""
        thisResult += '\t["'
        thisResult += name
        thisResult += '"] = \t\t {'
        
        browser.get("https://www.wowhead.com/object=" + href + "/")
        soup2 = BeautifulSoup(browser.page_source, 'html.parser')
        
        data2 = soup2.find_all("tbody", {"class":"clickable"})
        if len(data2) > 0:
            data2 = data2[0]
            for tr2 in data2.find_all('tr'):
                namecolumn = tr2.find_all("td")[2].find_all("a")[0]
                typecolumn = tr2.find_all("td")
                if len(typecolumn) >= 10:
                    typecolumn = typecolumn[9].find_all("a")[0]
                    if typecolumn.get_text() == "Herb":
                        empty = False
                        thisResult += re.search("[^\d+](\d+)[^\d+]", namecolumn.get("href")).group(1)
                        thisResult += ", "
        
        thisResult += '},\n'
        
        if not empty:
            previousName = name
            results += thisResult
            
            
url = "https://www.wowhead.com/objects/herbs#200+1+5"
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

data = soup.find_all("tbody", {"class":"clickable"})[0]
for tr in data.find_all('tr'):
    firstone = tr.find_all("td")[0].find_all("a")[0]
    name = firstone.get_text()
    if previousName != name:
        href = firstone.get("href")
        href = re.search("[^\d+](\d+)[^\d+]", href).group(1)
        empty = True
        thisResult = ""
        thisResult += '\t["'
        thisResult += name
        thisResult += '"] = \t\t {'
        
        browser.get("https://www.wowhead.com/object=" + href + "/")
        soup2 = BeautifulSoup(browser.page_source, 'html.parser')
        
        data2 = soup2.find_all("tbody", {"class":"clickable"})
        if len(data2) > 0:
            data2 = data2[0]
            for tr2 in data2.find_all('tr'):
                namecolumn = tr2.find_all("td")[2].find_all("a")[0]
                typecolumn = tr2.find_all("td")
                if len(typecolumn) >= 10:
                    typecolumn = typecolumn[9].find_all("a")[0]
                    if typecolumn.get_text() == "Herb":
                        empty = False
                        thisResult += re.search("[^\d+](\d+)[^\d+]", namecolumn.get("href")).group(1)
                        thisResult += ", "
        
        thisResult += '},\n'
        
        if not empty:
            previousName = name
            results += thisResult
            
            
url = "https://www.wowhead.com/objects/herbs#300+1+5"
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

data = soup.find_all("tbody", {"class":"clickable"})[0]
for tr in data.find_all('tr'):
    firstone = tr.find_all("td")[0].find_all("a")[0]
    name = firstone.get_text()
    if previousName != name:
        href = firstone.get("href")
        href = re.search("[^\d+](\d+)[^\d+]", href).group(1)
        empty = True
        thisResult = ""
        thisResult += '\t["'
        thisResult += name
        thisResult += '"] = \t\t {'
        
        browser.get("https://www.wowhead.com/object=" + href + "/")
        soup2 = BeautifulSoup(browser.page_source, 'html.parser')
        
        data2 = soup2.find_all("tbody", {"class":"clickable"})
        if len(data2) > 0:
            data2 = data2[0]
            for tr2 in data2.find_all('tr'):
                namecolumn = tr2.find_all("td")[2].find_all("a")[0]
                typecolumn = tr2.find_all("td")
                if len(typecolumn) >= 10:
                    typecolumn = typecolumn[9].find_all("a")[0]
                    if typecolumn.get_text() == "Herb":
                        empty = False
                        thisResult += re.search("[^\d+](\d+)[^\d+]", namecolumn.get("href")).group(1)
                        thisResult += ", "
        
        thisResult += '},\n'
        
        if not empty:
            previousName = name
            results += thisResult
            
            

results += "}"

output = open("enUS.lua", "w")
output.write(results.encode('cp1252', errors='replace').decode('cp1252'))
output.close()

browser.close()

