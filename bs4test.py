import requests
from bs4 import BeautifulSoup as bs

code=input("name")
a=requests.get("https://lolchess.gg/profile/kr/"+code)
req=a.text
soup=bs(req,'html.parser')
#더블업모드 티어 및 LP
b=soup.find_all('div','tier-ranked-info__tierlp mb-1')[1]
tier=b.find('strong').text
LP=b.find('span').text
tier.strip(' ')
LP.strip(' ')

print(type(tier))
print(LP)
