#Imports
import requests
from bs4 import BeautifulSoup
import re
import pandas

#Parses the webpage and returns html data
page = requests.get("https://docs.python.org/3/library/random.html")
soup = BeautifulSoup(page.content, "html.parser")
#Scapres the website for "dt" 
elements = soup.find_all("dt")
methods = re.findall('id="random.\w+', str(elements))

for i in range (len(methods)):
    methods[i] = methods[i][4:]

desc_elements = soup.find_all("dd")


methods_desc = []
for item in desc_elements:
    item = item.text
    item = item.replace("\n", " ")
    methods_desc.append(item)

print("\n\n")
for i in range (len(methods)):
    print(methods[i])
    print(methods_desc[i])
    print("\n")


data = pandas.DataFrame({'name': methods, 'description': methods_desc})
data.head()

data.to_csv("scraped_data.csv")