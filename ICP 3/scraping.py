import requests
from bs4 import BeautifulSoup

html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")

html = BeautifulSoup(html.text, 'html.parser')
print (html.find("title").string)
# links = html.find_all("a", href=True)
# for i in links:
#     print (i['href'])

for link in html.find_all('a'):
    print(link.get('href'))