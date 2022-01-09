# model.py

"""Think of this like the dft function, which always provides the same answer for a given input, and reads from
various molecular files. """

import json


def dftish(core, shell, dielectric, passivization, twodimensional) -> float:
    c = str(core)
    s = str(shell)
    d = str(dielectric)
    p = str(passivization)
    t = str(twodimensional)
    with open('cs.json') as cj:
        cs = json.load(cj)
    with open('diel.json') as dj:
        diel = json.load(dj)
    with open('twod.json') as tj:
        twod = json.load(tj)
    with open('lig.json') as lj:
        lig = json.load(lj)
        # print(lig)
    # print(cs)
    return -2 + 0.002*((float(cs[c]) * float(cs[s])) / 2 + (float(cs[c]) * float(cs[s]) * float(twod[t])) / (
        float(cs[c] + cs[s]))) * float(lig[p] + 1) / (100.0 - float(diel[d]) * 0.2)

def streamdft(inputarray) -> float:
    retlist = []
    with open('cs.json') as cj:
        cs = json.load(cj)
    with open('diel.json') as dj:
        diel = json.load(dj)
    with open('twod.json') as tj:
        twod = json.load(tj)
    with open('lig.json') as lj:
        lig = json.load(lj)
    for i in inputarray:
        c = str(i[0])
        s = str(i[1])
        d = str(i[2])
        p = str(i[3])
        t = str(i[4])
        retlist.append(-2 + 0.002*((float(cs[c]) * float(cs[s])) / 2 + (float(cs[c]) * float(cs[s]) * float(twod[t])) / (float(cs[c] + cs[s]))) * float(lig[p] + 1) / (100.0 - float(diel[d]) * 0.2))
    return retlist

if __name__ == "__main__":
    # print(dftish(1, 1, 1, 1, 1))
    pass
