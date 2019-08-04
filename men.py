from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://www.flipkart.com/mens-watches-store?otracker=nmenu_sub_Men_0_Watches")
soup = BeautifulSoup(html,'lxml')
dabba = soup.find_all('div', class_='_3liAhj _2Vsm67')

name=[]
price=[]
rating=[]
for i in dabba:
    n = i.find('a',class_='_2cLu-l')
    if n is None:
        name.append('NaN')
    else:
        name.append(n.text)
    p = i.find('div',class_='_1vC4OE')
    if p is None:
        price.append('NaN')
    else:
        price.append(p.text)
    r = i.find('div',class_='hGSR34')
    if r is None:
        rating.append('NaN')
    else:
        rating.append(r.text)

wpname=[]
wpprice=[]
wprating=[]
for x in name:
    wpname.append(x)
for x in price:
    wpprice.append(x)
for x in rating:
    wprating.append(x)
print(wpname)
print(wpprice)
print(wprating)

df = pd.DataFrame({'name':wpname, 'price':wpprice, 'rating':wprating})
print(df)