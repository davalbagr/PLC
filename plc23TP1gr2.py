import collections
import re
import networkx as nx
import matplotlib.pyplot as plt
import ftfy

f = open('arq-son.txt', 'r', encoding="utf-8")


def getProvince(line):
    return re.sub(r'\W', '', line[0], re.UNICODE)


def getLocal(line):
    pattern = r',\s*(.*)$'
    match = re.search(pattern, line[1])
    if match:
        return match.group(1)
    else:
        return line[1]


def getCancao(line):
    # TODO
    return re.match(r'[^;(]*', line[2]).group(0)

def getInstrumentos(line):
    # TODO
    return ""


def getCantores(line):
    # TODO
    res = [re.match(r'[^;(\s]*', i).group(0) for i in line[3].split(';')]
    return [i for i in res if i != '']


# Provincia::LocalOrig::Titulo::Musicos::SuporteDigital::...

s = ftfy.fix_text(f.read())
v = re.split(r'\n', s, flags=re.MULTILINE)
arr = [re.split('::', i) for i in v[1:]]
arr = [line[:-1] for line in arr]

for i in range(len(arr)-1, -1, -1):
    if len(arr[i]) < 6:
        del arr[i]

# ------------- a) -------------

prov = collections.defaultdict(int)
loc = collections.defaultdict(int)

for line in arr:
    prov[getProvince(line)] += 1
    loc[getLocal(line)] += 1

print("\nPROVINCIAS")
for i, j in prov.items():
    print(f"{i}: {j}")

print("\nLOCAIS")
for i, j in loc.items():
    print(f"{i}: {j}")
'''
# ------------- b) -------------

comMP3 = []

for line in arr:
    for i in line:
        if re.search(r'.mp3', line[-2]):
            comMP3.append(getCancao(line))
            break

for i in comMP3:
    print(i)

# ------------- c) -------------

intrumentos = {}
for line in arr:
    for i in getInstrumentos(line):
        intrumentos[i] += 1

for i, j in intrumentos.items():
    print(f'{i}: {j}')

# ------------- d) -------------

cantores = collections.defaultdict(int)

for line in arr:
    for i in getCantores(line):
        cantores[i] += 1

for i, j in cantores.items():
    print(f"{i}: {j}")

# ------------- e) -------------

adjList = collections.defaultdict(list)

for line in arr:
    cancao = getCancao(line)
    for i in getCantores(line):
        adjList[cancao].append(i)

for i, j in adjList.items():
    print(f'{i}: {j}')
'''

