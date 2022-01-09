# calc.py

"""
runs the actual mc simulation
"""

from model import dftish, streamdft
from data import *
from utils import *
import random
import matplotlib.pyplot as plt

DEBUG = True

def run(samples = 1000, gens=5000000):
    sortedlist = []
    streaminp = []
    gent = gens/10
    genh = gens/100
    for i in range(samples):
        z = [random.randint(1, gens), random.randint(1, gens), random.randint(1, gent), random.randint(1,genh),
                   random.randint(1, gent)]
        streaminp.append(z)

    sortedlist = streamdft(streaminp)
    for i in range(1000000):
        sortedlist.append(0)

    sortedlist.append(50)
    sortedlist.sort()
    if DEBUG:
        # print(sortedlist)
        plotout(sortedlist, title="Final Values")


def gen():
    generate(50000, 1000)




if __name__ == '__main__':
    run(1000000)
