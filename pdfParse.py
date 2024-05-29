import requests
from bs4 import BeautifulSoup

p = ''
people = []
purls = []
with open("cmww.html", "r") as pp:
    p = pp.read()
soup = BeautifulSoup(p, "html.parser")
people = soup.findAll('h3', class_='title')
for i in people:
    purls.append((i.findNext().get('href'), i.findNext().text))

for url in purls:
    r = requests.get(url[0]+'/download.pdf')
    with open(f'files/{url[1]}.pdf', 'wb') as f:
        f.write(r.content)