import numpy as np
import sympy as sym
from itertools import combinations

def readVault(textFile): # lee el vault capturado en un archivo de texto
  vault = []
  with open(textFile) as file:
    vault = [tuple(map(int, line.split(', '))) for line in file]
  return vault

def interpolation(xi, fi): # Polinomio de Lagrange
  xi = np.array(xi)
  fi = np.array(fi)

  n = len(xi)
  x = sym.Symbol('x')
  polinomio = 0
  divisorL = np.zeros(n, dtype = float)
  for i in range(0,n,1):
      # Termino de Lagrange
      numerador = 1
      denominador = 1
      for j  in range(0,n,1):
          if (j!=i):
              numerador = numerador*(x-xi[j])
              denominador = denominador*(xi[i]-xi[j])
      terminoLi = numerador/denominador

      polinomio = polinomio + terminoLi*fi[i]
      divisorL[i] = denominador

  # simplifica el polinomio
  polisimple = polinomio.expand()

  print('Polinomio de Lagrange: ')
  print(polisimple)

r = readVault("vault.txt") # total de puntos de la boveda
# k = grado del polinomio
# t = posibles puntos genuinos
for k in range(2, len(r)): # calcula el polinomio de lagrange con k puntos tomados del vault
  combinationsOfK = combinations(r, k)

  xi = []
  fi = []
  for subset in combinationsOfK:
    for t in subset:
      aux = list(t)
      xi.append(aux[0])
      fi.append(aux[1])
    print("xi = ", xi)
    print("fi = ", fi) 
    interpolation(xi, fi)
    xi.clear()
    fi.clear()
    #break