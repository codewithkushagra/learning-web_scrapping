import requests
from bs4 import BeautifulSoup

url="https://codewithharry.com"

content=requests.get(url)
c=content.content
#print(c)

soup=BeautifulSoup(c,'html.parser')
#print(soup.prettify)

paras=soup.find_all('p')
#print(paras)

anchors=soup.find_all('a')
#print(anchors)

all_link=set()

for link in anchors:
    if link.get('href')!='#':
        all_link.add("https://codewithharry.com"+link.get('href'))
print(all_link)

#print(soup.find('p'))
#print(soup.find('p')['class'])
#print(soup.find_all("p", class_="lead"))
#print(soup.find('p').get_text())
#print(soup.get_text())