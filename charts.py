import os
import matplotlib.pyplot as plt
import json, os
import numpy as np

def choice():
    a1 = int(input('Select option:\n'
                   '0 - Show crime chart\n'
                   '1 - Show countries chart\n'))
    print('Select json:')
    for i, e in enumerate(os.listdir('jsons/')):
        print(f'{i} - {e}')
    a2=int(input())
    if a1==0:
        if os.listdir('jsons/')[a2].split('_')[1] == 'crimes.json':
            crimesG(f"jsons/{os.listdir('jsons/')[a2]}")
        else:
            print('Wrong file')
            return
    if a1==1:
        if os.listdir('jsons/')[a2].split('_')[1] == 'countries.json':
            countriesG(f"jsons/{os.listdir('jsons/')[a2]}")
        else:
            print('Wrong file')
            return
def crimesG(dir):
    with open(dir) as f:
        data = json.load(f)

    nCrimes = {}
    for i in data.values():
        for j in i:
            if j not in nCrimes:
                nCrimes[j] = 1
            else:
                nCrimes[j] += 1

    nnCrimes = {'OTHER' : 0}
    oth = int(input('Select floor for OTHER (0 - every crime included, 5 - every crime above 5):\n'))
    for i in nCrimes:
        if nCrimes[i] > oth:
            nnCrimes[i] = nCrimes[i]
        else:
            nnCrimes['OTHER']+=1

    plt.pie(nnCrimes.values(), labels=nnCrimes.keys(), labeldistance=1.2, autopct='%1.2f%%', pctdistance=0.8, textprops={'fontsize':10}, wedgeprops = { 'linewidth' : 0.7, 'edgecolor' : 'white'})
    plt.show()

def countriesG(dir):
    with open(dir) as f:
        data2 = json.load(f)
    y_pos = np.arange(len(data2.keys()))
    height = data2.values()
    plt.bar(y_pos, height)
    plt.xticks(y_pos, data2.keys())
    plt.show()
