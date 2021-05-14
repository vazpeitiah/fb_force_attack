import numpy as np
import sympy as sympy
import math
from scipy.interpolate import lagrange
from itertools import combinations

import hashlib as hashlib

xiF = [20891, 20339, 4898, 59059, 59266, 39479, 18047, 9855, 29507]
fiF = [49661, 64551, 13405, 18972, 6786, 63594, 1284, 59927, 18676]
hF = hashlib.sha256(lagrange(xiF, fiF).__str__().encode('utf-8')).hexdigest()

def readVault(textFile):  # lee el vault capturado en un archivo de texto
    vault = []
    with open(textFile) as file:
        vault = [tuple(map(int, line.split(' '))) for line in file]
    return vault

r = readVault("vault/vault.txt")

print("Iniciando ataque de fuerza bruta")

for k in range(2, 9): # calcula el polinomio de lagrange con k puntos tomados del vault
    print("Probando combinaciones para k=", k)

    combinationsOfK = combinations(r, k + 1)
    for subset in combinationsOfK:
        xi = []
        fi = []
        for t in subset:
            aux = list(t)
            xi.append(aux[0])
            fi.append(aux[1])
        fa = lagrange(xi, fi)
        hfa = hashlib.sha256(fa.__str__().encode('utf-8')).hexdigest()
        # print(fa)
        if (np.array_equal(xi,xiF) and np.array_equal(fi,fiF)):
            print("Ok")
        if(hfa == hF):
            print("Se encontro el polinomio correcto:")
            print(fa)
            break
