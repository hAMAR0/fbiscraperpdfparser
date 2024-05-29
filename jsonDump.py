from pypdf import PdfReader
import os, json

def crimes():
    def visitor_body(text, cm, tm, font_dict, font_size):
        if (font_size == 12):
            parts.append(text.upper())
    d={}
    for i in os.listdir('files/'):
        parts = []
        reader = PdfReader(f"files/{i}")
        page = reader.pages[0]
        page.extract_text(visitor_text=visitor_body)
        a = ''.join(parts)
        if (a.find('DESCRIPTION') != -1):
            a = a.split('DESCRIPTION')[0]
        elif (a.find('CAUTION') != -1):
            a = a.split('CAUTION')[0]
        elif (a.find('DETAILS') != -1):
            a = a.split('DETAILS')[0]
        a = a.replace('\n', '')
        a = a.split('; ')
        a[-1] = a[-1].strip()
        d[i[:-4]] = a

    with open('data.json', 'w') as f:
        json.dump(d, f, indent=4)

def countriesf():
    def visitor_body2(text, cm, tm, font_dict, font_size):
        if (font_size == 8.25):
            parts.append(text.upper())
    d={}
    countries=[]
    places=[]
    for i in os.listdir('files/'):
        parts = []
        reader = PdfReader(f"files/{i}")
        page = reader.pages[0]
        page.extract_text(visitor_text=visitor_body2)
        a = ''.join(parts)
        places.append(a[a.find('PLACE OF BIRTH:'):].split('\n')[0])

    for j in places:
        if len(j)>0:
            countries.append(j.split(': ')[1])

    for i in range(len(countries)):
        if ',' in countries[i]:
            countries[i] = countries[i].split(',')[-1]
        if 'HAIR' in countries[i]:
            countries[i] = countries[i].replace('HAIR', '', 1)
        countries[i] = countries[i].replace(' ', '')
        if 'NORTHKOREA' in countries[i]:
            countries[i] = 'DPRK'
        if 'CHINA' in countries[i]:
            countries[i] = 'PRC'

    cntr = {}
    for i in countries:
        if i not in cntr:
            cntr[i] = 1
        else:
            cntr[i]+=1
    with open('dataCountries.json', 'w') as f:
        json.dump(cntr, f, indent=4)

