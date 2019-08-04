from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests

try:
    html = urlopen("https://www.wikipedia.org/robots.txt")
except:
    print("no such url exists")
else:
    print("url is opened")
finally:
    print("runs no matter what")
print("----------1"*5)
soup = bs(html, 'lxml')
pri = soup.prettify()
# print(pri)
print("----------2"*5)

data_gov = urlopen(
    "https://catalog.data.gov/dataset?q=&sort=metadata_created+desc&as_sfid=AAAAAAUbDk_MEYHbC2EkqaZNCbryCRXgPFYDQiikxHDp3l2OFHStzOiLXkhRKoiyJ-VEMfYeY_ZYfx07Zz4nVQo8SKsTDOvMiPz4BYqnLebnBfSlm4VHUstKwocGA9qMrsGlvVg%3D&as_fid=8c063dbdc7b373861e3f66b95ba7ccfa6dffafdf&ext_location=&ext_bbox=&ext_prev_extent=-142.03125%2C8.754794702435618%2C-59.0625%2C61.77312286453146")
soup2 = bs(data_gov, 'lxml')
dataset = soup2.find_all('div', class_='dataset-content')
print(dataset.__len__())
latest = dataset[0].text
print(latest)
print("----------5"*5)

example_url=urlopen("http://example.com/")
soup3 = bs(example_url,'lxml')
example = soup3.find('h1')
print(example.text)
print("----------6"*5)

header_url = urlopen("https://en.wikipedia.org/wiki/Main_Page")
soup4 = bs(header_url, 'lxml')
header=[]
list=['h1','h2','h3','h4','h5','h6']
for i in list:
    header.append(soup4.find_all(i))
for i in header:
    for j in i:
        print(j.text)
print("----------7"*5)

officer_url=urlopen("https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)")
soup5 = bs(officer_url, 'lxml')
officer=soup5.find_all('img')
for i in officer:
    print(i['src'])
print("----------8"*5)

browsers_url = requests.get("https://analytics.usa.gov/data/live/browsers.json")
print(browsers_url.json()['totals']['browser'])
print("----------9"*5)

python_url = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
python = bs(python_url,'lxml')
python_list = python.find_all('a')
for i in python_list:
    print(i.text)