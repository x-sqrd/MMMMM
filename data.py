# data.py

"""
Generates data points for each molecule, used before starting a mc session.
Utilize model.py to read this and create predictions used during mc session.
"""

from scipy.stats import binom
import json
import numpy as np

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

def generate(num=5000000, s=500):
    ntd = int(num/100)
    ntd2 = int(num/10)
    st = int(s/10)
    sh = int(s/100)
    cs_sample = binom.rvs(n=s, p=0.2, size=num)
    twod_sample = binom.rvs(n=s*20, p=0.7, size=ntd2)
    diel_sample = binom.rvs(n=st, p=0.8, size=ntd2)
    lig_sample = binom.rvs(n=sh, p=0.2, size=ntd)
    cs = dict(enumerate(cs_sample.flatten(), 1))
    twod = dict(enumerate(twod_sample.flatten(), 1))
    diel = dict(enumerate(diel_sample.flatten(), 1))
    lig = dict(enumerate(lig_sample.flatten(), 1))
    with open("cs.json", "w") as cso:
        json.dump(cs, cso, cls=NpEncoder)
    with open("twod.json", "w") as twodo:
        json.dump(twod, twodo, cls=NpEncoder)
    with open("diel.json", "w") as dielo:
        json.dump(diel, dielo, cls=NpEncoder)
    with open("lig.json", "w") as ligo:
        json.dump(lig, ligo, cls=NpEncoder)
    return [len(cs), len(cs), len(twod), len(diel), len(lig)]



if __name__ == "__main__":
    generate()