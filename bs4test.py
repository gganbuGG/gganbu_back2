import requests
import urllib.parse
from bs4 import BeautifulSoup as bs

code=input("name")
encode = urllib.parse.quote_plus(code)
a=requests.get("https://lolchess.gg/profile/kr/"+encode)
req=a.text
soup=bs(req,'html.parser')
#더블업모드 티어 및 LP
b=soup.find_all('div','tier-ranked-info__content')[1]
if b.find('strong'):
    tier=b.find('strong').text
    tier=str(tier).strip()
    LP=b.find('span').text
    LP=LP[:-2]

else:
    tier=b.find('span').text
    LP=0



print(str(tier))
print(int(LP))

