import requests, os
from bs4 import BeautifulSoup
import pagesaver as ps

urls = {}
urls['fugitives'] = ['https://www.fbi.gov/wanted/cac',
                     'https://www.fbi.gov/wanted/murders',
                     'https://www.fbi.gov/wanted/additional',
                     'https://www.fbi.gov/wanted/cyber',
                     'https://www.fbi.gov/wanted/wcc',
                     'https://www.fbi.gov/wanted/counterintelligence',
                     'https://www.fbi.gov/wanted/cei',
                     'https://www.fbi.gov/wanted/human-trafficking']
urls['terrorism'] = ['https://www.fbi.gov/wanted/wanted_terrorists',
                     'https://www.fbi.gov/wanted/terrorinfo',
                     'https://www.fbi.gov/wanted/dt']
urls['kidnapping'] = ['https://www.fbi.gov/wanted/kidnap',
                      'https://www.fbi.gov/wanted/parental-kidnappings']

def option():
    category = int(input('Select option:\n'
                         '0 - Fugitives\n'
                         '1 - Terrorism\n'
                         '2 - Kidnapping\n'))
    if category==0:
        print('Select option: ')
        for i, e in enumerate(urls['fugitives']):
            print(f'{i} - {e[27:]}')
        chCategory = int(input())
        print('Page downloading in proccess')
        ps.save(urls['fugitives'][chCategory])
        scrape(f"fugitives/{urls['fugitives'][chCategory][27:]}", len(urls['fugitives'][chCategory]))
    if category==1:
        print('Select option: ')
        for i, e in enumerate(urls['terrorism']):
            print(f'{i} - {e[27:]}')
        chCategory = int(input())
        print('Page downloading in proccess')
        ps.save(urls['terrorism'][chCategory])
        scrape(f"terrorism/{urls['terrorism'][chCategory][27:]}", len(urls['terrorism'][chCategory]))
    if category==2:
        print('Select option: ')
        for i, e in enumerate(urls['kidnapping']):
            print(f'{i} - {e[27:]}')
        chCategory = int(input())
        print('Page downloading in proccess')
        ps.save(urls['kidnapping'][chCategory])
        scrape(f"kidnapping/{urls['kidnapping'][chCategory][27:]}", len(urls['kidnapping'][chCategory]))
def scrape(dir,leng):
    dir1, dir2 = dir.split('/')
    if not os.path.isdir('files'):
        os.mkdir('files')
    if not os.path.isdir(f'files/{dir1}'):
        os.mkdir(f'files/{dir1}')
    if not os.path.isdir(f'files/{dir1}/{dir2}'):
        os.mkdir(f'files/{dir1}/{dir2}')
    purls = []
    with open("page.html", "r") as pp:
        p = pp.read()
    soup = BeautifulSoup(p, "html.parser")
    people = soup.findAll('h3', class_='title')
    for i in people:
        purls.append((i.findNext().get('href'), i.findNext().text))

    for i, url in enumerate(purls):
        r = requests.get(url[0]+'/download.pdf')
        u1 = url[1]
        if '"' in u1:
            u1=u1.replace('"','')
        with open(f'files/{dir}/{u1}.pdf', 'wb') as f:
            f.write(r.content)
            if (i+1) % 5 == 0:
                print(f'{i+1} completed')
    print('Success.')

option()