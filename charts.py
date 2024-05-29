import matplotlib.pyplot as plt
import json
import numpy as np

with open('data.json') as f:
    data = json.load(f)


nCrimes = {}
for i in data.values():
    for j in i:
        if j not in nCrimes:
            nCrimes[j] = 1
        else:
            nCrimes[j] += 1

nnCrimes = {'OTHER' : 0}
for i in nCrimes:
    if nCrimes[i] > 8:
        nnCrimes[i] = nCrimes[i]
    else:
        nnCrimes['OTHER']+=1

plt.pie(nnCrimes.values(), labels=nnCrimes.keys(), labeldistance=1.2, autopct='%1.2f%%', pctdistance=0.8, textprops={'fontsize':10}, wedgeprops = { 'linewidth' : 0.7, 'edgecolor' : 'white'})
plt.show()

with open('dataCountries.json') as f:
    data2 = json.load(f)
y_pos = np.arange(len(data2.keys()))
height = data2.values()
plt.bar(y_pos, height)
plt.xticks(y_pos, data2.keys())
plt.show()